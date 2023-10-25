from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
#print(soup)
#<table class="wikitable sortable jquery-tablesorter">
#<caption>
#print(soup.find_all('table')[1])
table = soup.find_all('table')[1]
soup.find_all('th')
#print(soup.find_all('th'))
world_titles = table.find_all('th')
world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)

import pandas as pd
df=pd.DataFrame(columns=world_table_titles)
#print(df)
column_data = table.find_all('tr')
#print(column_data)
for row in column_data[1:]:
    row_data=row.find_all('td')
    #print(row_data)
    individual_row_data=[data.text.strip() for data in row_data]
    #print(individual_row_data)
    
    length=len(df)
    df.loc[length]=individual_row_data
    #print(df)
df.to_csv(r'D:\Mine\GitHub\Lucky-repos\web_scrapping\top_companies.csv',index=False)
