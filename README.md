# 🛒 Simple Shop

This project integrates Stripe Checkout, offering a secure and efficient payment gateway. The user-friendly interface allows customers to easily purchase products. Please note that this is a demonstration project and not intended for actual commercial use.

## 🌟 Features

- **Secure Payments:** Seamless integration with Stripe Checkout for secure transactions.
- **Product Catalog:** Browse products with images, descriptions and pricing.

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (for development) / Heroku Postgres (for production)
- **Payment Integration:** Stripe Checkout
- **Deployment:** Heroku

## 🔧 Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/blakebrandon-hub/Simple-Shop.git
    cd Simple-Shop
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    - Create a `.env` file in the project root directory.
    - Add your Stripe API keys and other necessary configurations:

        ```env
        STRIPE_PUBLISHABLE_KEY=your_publishable_key
        STRIPE_SECRET_KEY=your_secret_key
        ```

5. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Populate the Database with Sample Products (Optional):**

    ```bash
    python populate_products.py
    ```

7. **Collect Static Files:**

    ```bash
    python manage.py collectstatic
    ```

8. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

9. **Access the Application:**

    - Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## ⚠️ Important Notes

- **Stripe Testing:** This project is configured to use Stripe's test mode. Use test card numbers provided by Stripe (e.g., `4242 4242 4242 4242`) for transactions. For more information, refer to Stripe's testing documentation: [Stripe Testing](https://stripe.com/docs/testing).

- **Deployment:** If deploying to a production environment, ensure that you set the `DEBUG` setting to `False`, configure allowed hosts, and use production-ready databases and Stripe keys.


