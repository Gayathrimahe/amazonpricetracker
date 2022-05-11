import requests
from bs4 import BeautifulSoup
import lxml


AMAZON_PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=dp_fod_2?pd_rd_i=B075CWJ3T8&th=1"

response = requests.get(AMAZON_PRODUCT_URL, headers={"Accept-Language": "en-US,en;q=0.9",
                                                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                                   "AppleWebKit/537.36 (KHTML, like Gecko)"
                                                                   " Chrome/100.0.4896.127 Safari/537.36"})
webpage_data = response.text
#print(webpage_data)
soup = BeautifulSoup(webpage_data, "lxml")
result = soup.find("span", class_="a-offscreen")
float_price = float(result.getText().split("$")[1])
print(float_price)


#####SMTP mailing is pending

