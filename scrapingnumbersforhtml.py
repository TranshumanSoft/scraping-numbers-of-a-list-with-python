from urllib import request
from bs4 import BeautifulSoup
import ssl
#You must ignore SSL certificate errors.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
html = request.urlopen("http://py4e-data.dr-chuck.net/comments_288692.html", context = context).read()
soup = BeautifulSoup(html)
tags = soup("span")
sum = 0
for tag in tags:
    number = int(tag.contents[0])
    sum = sum + number
print(f"The sum of all the comments is: {sum}")