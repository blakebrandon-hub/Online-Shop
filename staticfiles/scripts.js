document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartNumber = document.getElementById('cart-number');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    let cartItems = [];

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productName = button.getAttribute('name');
            let price_id = "";

            // Define price_id based on productName
            switch (productName) {
                case 'Jeans':
                    price_id = 'price_1PrIciEN9TFKicCw3UPuYv2q';
                    break;
                case 'Hooded Sweatshirt':
                    price_id = 'price_1PrIiQEN9TFKicCwTCR7lOCs';
                    break;
                case 'Shorts':
                    price_id = 'price_1PrIhpEN9TFKicCwRAfU8eVr';
                    break;
                case 'Socks':
                    price_id = 'price_1PrIgkEN9TFKicCwpMcLTIEL';
                    break;
                case 'Hat':
                    price_id = 'price_1PrIfMEN9TFKicCwvJ3iL9yS';
                    break;
                case 'Jacket':
                    price_id = 'price_1PrIerEN9TFKicCwj60Zne0x';
                    break;
                case 'Sneakers':
                    price_id = 'price_1PrIeLEN9TFKicCwmkyhQPIm';
                    break;
                case 'T-shirt':
                    price_id = 'price_1PrIaMEN9TFKicCwDW2XyjrW';
                    break;
                default:
                    return; 
            }

            // Add price_id to cartItems list
            if (button.textContent.trim() === 'Add to cart') {
                count++;
                cartItems.push(price_id);
                button.textContent = 'Remove from cart';
            } else {
                count--;
                cartItems = cartItems.filter(item => item !== price_id);
                button.textContent = 'Add to cart';
            }

            cartNumber.textContent = count;
        });
    });

document.getElementById('checkout_button').addEventListener('click', function() {
    fetch('/create_checkout_session/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ price_ids: cartItems })
    })
    .then(response => response.json())
    .then(data => {
        if (data.id) {
            // Redirect to Stripe Checkout
            const stripe = Stripe('pk_test_51KLvUgEN9TFKicCwT1Owl6YPE9FIzhh4nhJECAR0eqVicJHpLfFlJnK5ZiMbwP6rhIhHjAgBILCY5iw7Rp5NTNdS00YnKgJI75');
            stripe.redirectToCheckout({ sessionId: data.id });
        } else {
            console.error('Error creating checkout session:', data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});
});