document.addEventListener("DOMContentLoaded", () => {
  const mainImg  = document.getElementById("painting-main-img");
  const mainLink = document.getElementById("painting-main-link");

  document.querySelectorAll(".thumbnail-link").forEach(link => {
    link.addEventListener("click", evt => {
      evt.preventDefault();            // не открывать ссылку
      const thumbImg = link.querySelector("img");
      mainImg.src      = thumbImg.dataset.full || link.href; // показываем HQ-кадр
      mainLink.href    = link.href;     // чтобы лайтбокс открыл корректное фото
    });
  });
});

document.querySelectorAll(".thumbnail").forEach(img => img.classList.remove("selected"));
thumbImg.classList.add("selected");
