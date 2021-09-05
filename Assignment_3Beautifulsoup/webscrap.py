from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas
import pandas as pd
import requests

req = requests.get(
    "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=0087ba24-a049-4fe4-b092-9f720c62711d&as-searchtext=lap")
content = req.content

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())

desc = soup.findAll('div', class_='_4rR01T')

description = []
for i in range(len(desc)):
    description.append(desc[i].text)
len(description)

commonclass = soup.findAll('li', class_='rgWa7D')

processors = []
ram = []
os = []
storage = []
inches = []
warranty = []

for i in range(0, len(commonclass)):
    p = commonclass[i].text  # Extracting the text from the tags
    if ("Core" in p):
        processors.append(p)
    elif ("RAM" in p):
        ram.append(p)
    # If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well
    elif ("HDD" in p or "SSD" in p):
        storage.append(p)
    elif ("Operating" in p):
        os.append(p)
    elif ("Display" in p):
        inches.append(p)
    elif ("Warranty" in p):
        warranty.append(p)

print(len(processors))
print(len(warranty))
print(len(os))
print(len(ram))
print(len(inches))

price = soup.find_all('div', class_='_30jeq3 _1_WHN1')
# Extracting price of each laptop from the website
prices = []
for i in range(len(price)):
    prices.append(price[i].text)
len(prices)

rating = soup.findAll('div', class_='_3LWZlK')
ratings = []
for i in range(len(rating)):
    ratings.append(rating[i].text)
ratings
len(ratings)


d = {'Description':description,'Processor':processors,'RAM':ram,'Operating System':os,'Storage':storage,'Display':inches,'Warranty':warranty,'Price':prices}
dataset = pd.DataFrame.from_dict(d, orient='index')# Finally merging all the features into a single dataframe
print(dataset)
dataset=dataset.transpose()


dataset.to_csv('laptop.csv')
df = pd.read_csv('laptop.csv')
df.shape

