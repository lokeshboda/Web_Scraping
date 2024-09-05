
document.addEventListener("DOMContentLoaded", () => {
const mobileMenu = document.querySelector(".mobile-menu"); const menu = document.querySelector(".menu");

mobileMenu.addEventListener("click", () => { menu.classList.toggle("show");
});


// Carousel Controls
const prevBtn = document.querySelector(".prev"); const nextBtn = document.querySelector(".next"); const carousel = document.querySelector(".carousel"); let index = 0;

function showSlide(i) {
const items = carousel.children; if (i >= items.length) {
index = 0;
}

if (i < 0) {
index = items.length - 1;
}
for (let item of items) { item.style.display = "none";
}
items[index].style.display = "block";
}


showSlide(index);


prevBtn.addEventListener("click", () => { index--;
showSlide(index);
});


nextBtn.addEventListener("click", () => { index++;
showSlide(index);
});
});