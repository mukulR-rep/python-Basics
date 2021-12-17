import requests
from bs4 import BeautifulSoup
req = requests.get(" https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/")
soup = BeautifulSoup(req.content, "html.parser")
print(soup.get_text())