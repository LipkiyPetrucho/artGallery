import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from show.models import Exhibition, VideoItem
from .models import Painting
from .forms import ContactForm

logger = logging.getLogger(__name__)


def home_view(request):
    return render(request, "artworks/home.html")


def about_view(request):
    return render(request, "artworks/about.html",{
        'exhibitions': Exhibition.objects.all(),  # type: ignore[attr-defined]
        'videos':       VideoItem.objects.all(),  # type: ignore[attr-defined]
    })


def gallery_view(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 15)

    page = request.GET.get('page')
    images_only = request.GET.get('images_only')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        if images_only:  # бесконечный скролл достиг конца
            return HttpResponse('')
        page_obj = paginator.page(paginator.num_pages)

    ctx = {'section': 'gallery', 'images': page_obj}

    if images_only:  # ajax-вариант
        return render(request,
                      'artworks/list_images.html',
                      ctx)

    # обычный первый заход
    return render(request,
                  'artworks/list.html',
                  ctx)


def contacts_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            attachment = form.cleaned_data.get("attachment")

            subject = f"Новое сообщение от {name}"
            body = f"Имя: {name}\nEmail: {from_email}\n\nСообщение:\n{message}"

            # Диагностические принты перед созданием EmailMessage
            print(f"Subject: {subject}")
            print(f"Body: {body}")
            print(f"From Email: {settings.DEFAULT_FROM_EMAIL}")
            print(f"To: {settings.ARTIST_EMAIL}")
            print(f"Reply To: {from_email}")

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ARTIST_EMAIL],
                reply_to=[from_email],
            )

            if attachment:
                email.attach(
                    attachment.name, attachment.read(), attachment.content_type
                )

            try:
                # Попытка отправки email
                print("Пытаемся отправить письмо...")
                email.send()
                print("Письмо успешно отправлено!")
                messages.success(request, "Ваше сообщение успешно отправлено!")
                return redirect("artworks:contacts")
            except Exception as e:
                # Диагностика ошибок отправки
                print("Ошибка при отправке письма!")
                print(f"Исключение: {e}")
                messages.error(
                    request,
                    "Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.",
                )
        else:
            print("Форма недействительна!")
            print(f"Ошибки формы: {form.errors}")
    else:
        form = ContactForm()

    return render(request, "artworks/contacts.html", {"form": form})


def free_works(request):
    paintings = Painting.objects.filter(status=Painting.Status.AVAILABLE)  # type: ignore[attr-defined]
    return render(request, "artworks/free_works.html", {"paintings": paintings})


def painting_detail(request, id):
    painting = get_object_or_404(
        Painting.objects.prefetch_related("extra_images"), id=id
    )
    # Получаем три случайные другие картины, исключая текущую
    other_paintings = Painting.objects.exclude(id=painting.id).order_by("?")[:3]  # type: ignore[attr-defined]
    return render(
        request,
        "artworks/detail.html",
        {"painting": painting, "other_paintings": other_paintings},
    )
