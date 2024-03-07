// script.js
window.addEventListener('load', function() {
    adjustImagePlacement();
});

function adjustImagePlacement() {
    var gallery = document.getElementById('gallery');
    var images = gallery.getElementsByTagName('img');

    var totalWidth = 0;
    for (var i = 0; i < images.length; i++) {
        totalWidth += images[i].offsetWidth;
    }

    var availableWidth = gallery.offsetWidth;
    var imagesPerRow = Math.floor(availableWidth / (images[0].offsetWidth + 20));

    var margin = (availableWidth - (imagesPerRow * images[0].offsetWidth)) / (6 * imagesPerRow);

    for (var i = 0; i < images.length; i++) {
        images[i].style.marginLeft = margin + 'px';
        images[i].style.marginRight = margin + 'px';
    }
}