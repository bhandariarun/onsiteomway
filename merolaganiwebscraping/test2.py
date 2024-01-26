from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import sqlite3
import csv



# site url
url="https://merolagani.com/LatestMarket.aspx"

# make a get request to fetch the raw html data
con=requests.get(url)
soup=BeautifulSoup(con.text)
x = soup.find('div',id='ctl00_ContentPlaceHolder1_LiveSectors')
table=x.find('table',class_='table table-hover')
headers=[i.text for i in table.find_all('th')]
data=[j.text for j in table.find_all('td')]
output_data = [headers]


for i in range(0, len(data), len(headers)):
        row = data[i:i + len(headers)]
        output_data.append(row)

for row in output_data:
    print(row)
#
df=pd.DataFrame(output_data)
# df
# df_cleaned = df.applymap(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x) if isinstance(x, str) else x)
# df.to_csv("merolaganidata1.csv", index=False)

csv_file_path = 'output.csv'

# Write to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

print(f'Data has been saved to {csv_file_path}')

df.to_csv("output.csv", index=False)
conn = sqlite3.connect('D:\SQLDatabase/turnovers.db')
cursor = conn.cursor()
df.to_sql('turnover', conn, index=False, if_exists='replace')
conn.commit()
conn.close()