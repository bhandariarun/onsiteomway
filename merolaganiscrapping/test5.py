from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import sqlite3



# site url
url="https://merolagani.com/LatestMarket.aspx"

# make a get request to fetch the raw html data
con=requests.get(url)
soup=BeautifulSoup(con.text)
table=soup.find('table',class_='table table-hover live-trading sortable')
# print(table)
headers=[i.text for i in table.find_all('th')]
# print(headers)
data=[j for j in table.find_all('tr',{'class':["decrease-row"]})]
# print(data)
result=[{headers[index]:cell.get_text(strip=True, separator=' ') for index,cell in enumerate(row.find_all('td'))} for row in data]
print(result)
df=pd.DataFrame(result)
df
df_cleaned = df.applymap(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x) if isinstance(x, str) else x)
df.to_csv("merolaganidata.csv", index=False)
conn = sqlite3.connect('D:\SQLDatabase/top.db')
cursor = conn.cursor()
df.to_sql('looser', conn, index=False, if_exists='replace')
conn.commit()
conn.close()
