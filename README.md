# E-Commerce Price Tracker Bot 📉

An automated Python script that monitors product prices on e-commerce websites (specifically configured for Kitapyurdu) and sends email notifications via SMTP when a price drop occurs.

## Tech Stack
* **Python 3.9.0
* **BeautifulSoup4** (Web Scraping)
* **Requests** (HTTP Requests)
* **smtplib** (Email Automation)

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/suedbn/ecommerce-price-tracker.git](https://github.com/suedbn/ecommerce-price-tracker.git)
2.Install required libraries: pip install requests beautifulsoup4 lxml
3.Configure Security (Critical Step): Open the main.py file in your code editor. Locate the configuration section at the top and update it with your own credentials:
  sender_mail = "your_email@gmail.com"
  sender_password = "YOUR_GOOGLE_APP_PASSWORD" # Paste your 16-digit App Password here
  receiver_mail = "your_email@gmail.com"
⚠️ Security Note: Do not use your standard Gmail login password. You must generate a specific Google App Password for this script to work securely.
4.Run the script: python main.py

⚠️ Disclaimer -> This project is developed for educational purposes to demonstrate web scraping and automation concepts. Please respect the robots.txt policy and Terms of Service of the target websites.
