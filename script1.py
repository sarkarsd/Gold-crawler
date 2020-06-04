import requests
from bs4 import BeautifulSoup
import pandas

df = pandas.DataFrame(columns=['Date', '22 Carat', '24 Carat'])
r = requests.get("https://www.goodreturns.in/gold-rates/kolkata.html")
c = r.content
print()
soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class": "gold_silver_table gold_silver_table_10_days"})

rows = all[0].find_all("td", {"class": ""})

arr = []
for i in range(len(rows)):
    arr.append(rows[i].text.replace("\t", "").replace("\n", "").replace("(%s)", ""))

for i in range(0, len(arr), 3):
    df = df.append({"Date": arr[i], "22 Carat": arr[i + 1], "24 Carat": arr[i + 2]}, ignore_index=True)

df.to_csv("Gold_Price_10g_Kolkata.csv")
print(arr)
