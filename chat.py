import requests
from bs4 import BeautifulSoup

class AmazonPriceChecker:
    def __init__(self, buy_price, url):
        self.buy_price = buy_price
        self.url = url

    def get_soup(self):
        header = {
            "Accept-language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }
        response = requests.get(url=self.url, headers=header)
        soup = BeautifulSoup(response.content, "lxml")
        return soup

    def get_price(self):
        soup = self.get_soup()
        price_text = soup.find(name="span", class_="a-price-whole").get_text()
        price = float(price_text)
        return price

    def check_price(self):
        price = self.get_price()
        if price < self.buy_price:
            return price
        else:
            return None


# Usage example
BUY_PRICE = 275
url = "https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV/ref=sr_1_3?crid=1BZ7XTE5JWT65&keywords=bose%2Bnoise%2Bcancelling%2Bheadphones%2B700&qid=1698077527&s=electronics&sprefix=bose%2Bnoi%2Celectronics%2C177&sr=1-3&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&th=1"

amazon_checker = AmazonPriceChecker(BUY_PRICE, url)
price_below_threshold = amazon_checker.check_price()

if price_below_threshold is not None:
    print(f"Price is below threshold: {price_below_threshold}")
else:
    print(f"No email sent. The price is above your set Buy Price: {BUY_PRICE}")
