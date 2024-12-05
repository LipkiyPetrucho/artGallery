import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Post

logger = logging.getLogger(__name__)


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)  # 5 постов на страницу
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)

    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    # Получаем другие посты для отображения миниатюр
    other_posts = (
        Post.published.all()[:3]
    )
    return render(
        request, "blog/post_detail.html", {"post": post, "other_posts": other_posts}
    )
