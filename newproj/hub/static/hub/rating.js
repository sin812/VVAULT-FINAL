document.addEventListener('DOMContentLoaded', function() {
    const buyNowButton = document.getElementById('buy-now');
    const cartPopup = document.getElementById('cart-popup');
    const closePopupButton = document.getElementById('close-popup');
    const closePopupBtn = document.getElementById('close-popup-btn');
    const goToCartButton = document.getElementById('go-to-cart');

    if (buyNowButton) {
        buyNowButton.addEventListener('click', function() {
            cartPopup.style.display = 'flex';
        });
    }

    if (closePopupButton) {
        closePopupButton.addEventListener('click', function() {
            cartPopup.style.display = 'none';
        });
    }

    if (closePopupBtn) {
        closePopupBtn.addEventListener('click', function() {
            cartPopup.style.display = 'none';
        });
    }

    if (goToCartButton) {
        goToCartButton.addEventListener('click', function() {
            window.location.href = '/cart/';
        });
    }
});
