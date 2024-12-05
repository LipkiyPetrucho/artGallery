document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('lightbox-modal');
    const modalImg = document.getElementById('lightbox-image');
    const captionText = document.getElementById('lightbox-caption');
    const closeBtn = document.getElementsByClassName('close')[0];
    const prevBtn = document.querySelector('.lightbox-navigation .prev');
    const nextBtn = document.querySelector('.lightbox-navigation .next');
    const container = document.querySelector('.container');

    // Собираем все полноразмерные изображения галереи
    const galleryImages = Array.from(document.querySelectorAll('.gallery-image')).map(a => a.dataset.full);
    const totalImages = galleryImages.length;
    let currentIndex = 0;

    // Обработчик клика на изображение галереи
    document.querySelectorAll('.gallery-image').forEach((link, index) => {
        console.log('Initializing gallery image:', index);
        link.addEventListener('click', function(event) {
            event.preventDefault();
            currentIndex = index;
            openModal();
            showImage(currentIndex);
        });
    });

    // Функция открытия модального окна
    function openModal() {
        modal.style.display = 'flex'; // Используем flex для центрирования
        container.classList.add('blurred');
    }

    // Функция закрытия модального окна
    function closeModal() {
        modal.style.display = 'none';
        container.classList.remove('blurred');
    }

    // Функция отображения изображения по индексу
    function showImage(index) {
        modalImg.src = galleryImages[index];
        captionText.textContent = `${index + 1} из ${totalImages}`;
    }

    // Обработчики кнопок навигации
    prevBtn.addEventListener('click', function(event) {
        event.stopPropagation(); // Предотвращаем закрытие модального окна при клике на стрелки
        currentIndex = (currentIndex === 0) ? totalImages - 1 : currentIndex - 1;
        showImage(currentIndex);
    });

    nextBtn.addEventListener('click', function(event) {
        event.stopPropagation();
        currentIndex = (currentIndex === totalImages - 1) ? 0 : currentIndex + 1;
        showImage(currentIndex);
    });

    // Обработчик кнопки закрытия
    closeBtn.addEventListener('click', function(event) {
        event.stopPropagation();
        closeModal();
    });

    // Закрытие модального окна при клике вне изображения
    modal.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    // Закрытие модального окна при нажатии клавиши Esc
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeModal();
        }
        // Добавляем возможность навигации с помощью стрелок
        if (modal.style.display === 'flex') {
            if (event.key === 'ArrowLeft') {
                currentIndex = (currentIndex === 0) ? totalImages - 1 : currentIndex - 1;
                showImage(currentIndex);
            }
            if (event.key === 'ArrowRight') {
                currentIndex = (currentIndex === totalImages - 1) ? 0 : currentIndex + 1;
                showImage(currentIndex);
            }
        }
    });
});
