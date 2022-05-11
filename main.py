import requests
from bs4 import BeautifulSoup
import lxml


AMAZON_PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=dp_fod_2?pd_rd_i=B075CWJ3T8&th=1"

response = requests.get(AMAZON_PRODUCT_URL, headers={"Accept-Language": "en-US,en;q=0.9",
                                                     "User-Agent": "YOUR HTTP HEADERS"})
webpage_data = response.text
#print(webpage_data)
soup = BeautifulSoup(webpage_data, "lxml")
result = soup.find("span", class_="a-offscreen")
float_price = float(result.getText().split("$")[1])
print(float_price)


#####SMTP mailing is pending
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
