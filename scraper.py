# Welcome to the Amazon product price webscraper!
# This webscraper takes a given Amazon product and sends an email from a specified address to another
# specified address when the price of the product drops belowed a specified price.

# For this to work, you must have access to the following information:
# 1. Amazon URL of the product whose price you'd like to track.
# 2. Your user agent. This can be found by googling "my user agent" and copying the string that pops up.
# 3. The sender's address. This email should be a gmail address that you can log into.
#    In addition, you must retrive an App Password which can be done by following the steps
#    at the following link: https://support.google.com/accounts/answer/185833?hl=en
#    For the app, choose mail, and for the device, choose whatever device you are using.
# 4. The receiver's address. This email can be any gmail address and will receive the price drop message.

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Enter the product URL
URL = 'https://www.amazon.ca/QUEST-NUTRITION-Tortilla-Style-Protein/dp/B07DHRV79M/ref=sr_1_6?dchild=1&keywords=protein+chips&qid=1594080571&sr=8-6'

# Enter your user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[4:])

    if(converted_price <= 3): # Replace this number with the maximum price of which you would like to buy the product at.
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Enter the sender's address below and the App Password below. Format: ('sender address', 'app password')
    server.login('rajangrewal123@gmail.com', 'djdcvfduytvrobbz')
    subject = 'Price has dropped!'     # Replace the link below with your product's link.
    body = 'Check the following link: https://www.amazon.ca/QUEST-NUTRITION-Tortilla-Style-Protein/dp/B07DHRV79M/ref=sr_1_6?dchild=1&keywords=protein+chips&qid=1594080571&sr=8-6'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'rajangrewal123@gmail.com', # Replace this with the sender's address.
        'rajangrewal1234@gmail.com', # Replace this with the receiver's address.
        msg
    )
    print("Email has been sent")
    server.quit()
while(1):
    check_price()
    time.sleep(60) # Enter how often you'd like the program to check the price (in seconds).