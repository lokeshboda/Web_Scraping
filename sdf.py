import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='KzDlHZ')
print(names)
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)

ratings=soup.find_all('div',class_='XQDdHH')
print(ratings)
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(float(d))
print(rating)

reviews=soup.find_all('span',class_='Wphh3N')
print(reviews)
review=[]
for i in reviews[0:10]:
    d=i.get_text()
    review.append(d)
print(review)

features=soup.find_all('ul',class_='G4BRas')
print(features)
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
print(feature)



images=soup.find_all('img',class_='DByuf4')
print(images)
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)


data={'Name':name,'Rating':rating,'Reviews':review,'Features':feature,'Images':image}
print(data)
df=pandas.DataFrame(data)
print(df)
df.to_csv("Mobiles_data.CSV")