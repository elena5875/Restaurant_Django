window.addEventListener('load', function() {
    adjustGalleryImages();
    window.addEventListener('resize', adjustGalleryImages);
});

function adjustGalleryImages() {
    var gallery = document.querySelector('.gallery-images');
    var images = gallery.getElementsByTagName('img');

    if (window.innerWidth <= 600) {
        for (var i = 0; i < images.length; i++) {
            if (i >= 6) {
                images[i].style.display = 'none';
            } else {
                images[i].style.display = 'block';
            }
        }
    } else {
        for (var i = 0; i < images.length; i++) {
            images[i].style.display = 'block';
        }
    }
}
