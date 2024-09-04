let currentIndex = 0;

function showNextImage() {
    const images = document.querySelectorAll('.image-slider img');
    images[currentIndex].style.transform = 'translateX(-100%)';
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.transform = 'translateX(0)';
}

setInterval(showNextImage, 3000);
