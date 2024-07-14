document.addEventListener('DOMContentLoaded', function() {
    console.log('Document is ready');
    var scrollToTopButton = document.getElementById('scroll-to-top');
    if (scrollToTopButton) {
        console.log('Button found');
        scrollToTopButton.addEventListener('click', function() {
            console.log('Button clicked');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    } else {
        console.log('Button not found');
    }
});
