
 # This program helps to understand a simple webScraping on Flipkart(Iphone models)
import requests
from bs4 import BeautifulSoup as soup
import csv

models =[]
prices =[]
ratings =[]

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
resp = requests.get(my_url)
htmlcontent = resp.content

# parse with inbuilt html parser
page_soup = soup(htmlcontent,'html.parser')
# use the main div tag
data_div = page_soup.find_all("div",attrs={"class":"_3pLy-c row"})

# loop the model div the find the similar elements
for x in data_div:
    model = x.find("div",attrs={"class":"_4rR01T"})
    price = x.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
    rating = x.find("div", attrs={"class": "_3LWZlK"})


    models.append(model.string)
    prices.append(price.string)
    ratings.append(rating.text)

header = ['Models','Prices','Ratings']
data = [models,prices,ratings]
print(data)
# excel generation
with open("sample.csv","w",encoding="utf-8") as fp:
    write=csv.writer(fp)
    write.writerow(header)
    write.writerows(data)

print("done.....................")

