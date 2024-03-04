// script.js


<!-- JavaScript for dynamically aligning images -->
<script>
window.addEventListener('load', function() {
    alignImages();
});

window.addEventListener('resize', function() {
    alignImages();
});

function alignImages() {
    var gallery = document.getElementById('gallery');
    var galleryImages = gallery.querySelectorAll('.gallery-images img');

    // Get the width of the container
    var containerWidth = gallery.offsetWidth;

    // Get the width of each image
    var imageWidth = galleryImages[0].offsetWidth;

    // Calculate the number of images per row
    var imagesPerRow = Math.floor(containerWidth / imageWidth);

    // Calculate the margin between images
    var margin = (containerWidth - (imagesPerRow * imageWidth)) / (imagesPerRow - 1);

    // Apply margin to images except for the last one in each row
    for (var i = 0; i < galleryImages.length; i++) {
        if (i % imagesPerRow !== imagesPerRow - 1) {
            galleryImages[i].style.marginRight = margin + 'px';
        } else {
            galleryImages[i].style.marginRight = 0;
        }
    }
}
</script>

