let currentSlide = 0;
const slides = document.querySelectorAll('.carousel .slide');
const totalSlides = slides.length;

function showSlide(slideIndex) {
    slides.forEach((slide, index) => {
        slide.style.display = index === slideIndex ? 'block' : 'none';
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

setInterval(nextSlide, 3000); // Change slide every 3 seconds

document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentSlide);
});
