# E-commerce Website

Welcome to E-commerce Website, an e-commerce platform designed to offer users a streamlined online shopping experience. This project is part of my portfolio and showcases the integration of secure payment solutions with a user-friendly interface.

## Features

- **Secure Payments**: Integrated with Stripe Checkout for secure and efficient transactions.
- **Product Browsing**: Display products with detailed descriptions and pricing.
- **Product Filtering**: Filter products based on categories directly from the navbar.
- **User-Friendly Design**: Clean and responsive UI for seamless navigation across devices.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (development) / Heroku Postgres (production-ready)
- **Payment Integration**: Stripe Checkout
- **Deployment**: Heroku

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/blakebrandon-hub/Simple-Shop.git
   cd Simple-Shop
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Stripe API keys and other sensitive configurations:
   ```env
   STRIPE_PUBLIC_KEY=your_stripe_public_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Visit `http://127.0.0.1:8000` in your browser.

## Deployment

The project is deployed on Heroku. To deploy your own instance:

1. Push the code to your Heroku repository.
2. Configure Heroku environment variables for Stripe keys and Django settings.
3. Use Heroku Postgres for production by updating the database settings.
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

## Usage

- Browse and select products.
- Add products to your cart.
- Checkout using Stripe for secure payments.

### Home Page
![Home Page Screenshot](https://via.placeholder.com/800x400?text=Home+Page+Screenshot)

### Product Page
![Product Page Screenshot](https://via.placeholder.com/800x400?text=Product+Page+Screenshot)

### Checkout Page
![Checkout Page Screenshot](https://via.placeholder.com/800x400?text=Checkout+Page+Screenshot)

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or suggestions, contact me:
- **GitHub**: [blakebrandon-hub](https://github.com/blakebrandon-hub)
- **Email**: blakebrandon.dev@gmail.com

---



