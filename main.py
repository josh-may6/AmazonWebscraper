from bs4 import BeautifulSoup
import requests
from notification import Email
import time
import schedule


def price_check(buy_price):
    url = "https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV/ref=sr_1_3?crid=1BZ7XTE5JWT65&keywords=bose%2Bnoise%2Bcancelling%2Bheadphones%2B700&qid=1698077527&s=electronics&sprefix=bose%2Bnoi%2Celectronics%2C177&sr=1-3&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&th=1"
    header = {
        "Accept-language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    response = requests.get(url=url, headers=header)

    soup = BeautifulSoup(response.content, "lxml")

    price_text = soup.find(name="span", class_="a-price-whole").get_text().strip()
    price_text_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
    str_price = price_text + price_text_fraction
    price = float(price_text + price_text_fraction)

    if price < buy_price:
        email = Email(price=price, link=url)
        email.send_email()
        print(price)
    else:
        print(f"No email sent. The price is: {str_price}. Which is above your set Buy Price: {buy_price:.02f}")


price_check(300)
