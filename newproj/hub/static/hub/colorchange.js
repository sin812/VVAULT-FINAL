document.addEventListener("DOMContentLoaded", function() {
    const vinyls = document.querySelectorAll(".vinyl");

    vinyls.forEach(vinyl => {
        const dominantColor = vinyl.getAttribute("data-dominant-color");
        console.log(`Vinyl: ${vinyl}, Dominant Color: ${dominantColor}`); // Debug log
        vinyl.style.setProperty("--dominant-color", dominantColor);
    });
});


