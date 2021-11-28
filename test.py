import requests
import csv


rows = []
eligible_countries = []
url = input('Webpage to grab source from: ')
html_output_name = input('Name for html file: ')


req = requests.get(url, 'html.parser')


with open(html_output_name, 'r') as f:
    f.read(req.text)
for row in req.text:
    rows.append(row)
input = int(input("Please enter the limit of population: "))
eligible_countries = []
for i in rows:
  if source[i][2] < input:
    eligible_countries.append(rows[i])
print(eligible_countries)
f.close()
source = []