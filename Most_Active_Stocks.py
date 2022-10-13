from pydoc import classify_class_attrs
import pandas as pd
import requests
from bs4 import BeautifulSoup

# get bloomberg page
original = requests.get('https://www.webull.com/quote/us/etfs')
original
original.text


# Create a BeautifulSoup object
soup = BeautifulSoup(original.text, 'html.parser')  ### get repo descriptions

# print pretty
print(soup.prettify())

# CREATE DATAFRAME 

stock_name = soup.find_all('p', class_='tit bold')

stock_names = []

for item in stock_name:
    name = item.text 
    #print('Part 1: Raw: ', name)
    
    ## clean name remove upper whitespace or blank space that exist at the top
    name = name.strip()   
    #print('Part 2: Updated: ', name)
    
    ## remove new line, and replace with no spae (whitespace) or remove additional lines that exists and push everything into single line
    name = name.replace('\n','')
    #print('Part 3: Updated: ', name)
    
    ## remove all white space
    name = name.replace(' ','')
    #print('Part 4: Updated: ', name)
    stock_names.append(name)

len(stock_names)

for names in stock_names:    #  to loop through repo underscore names and just print each of the items that exists within that list
    print(names)
    
    
    ## 2nd dataset 
stock_price = soup.find_all('div', class_='table-cell')

stock_prices = []

for item in stock_price:         
    name = item.text
    #print('Part 1: Raw: ', name)
    ## clean name remove whitespace
    name = name.strip()         # remove white space but indent remains
    #print('Part 2: Updated: ', name)
    ## remove new line
    name = name.replace('\n','')    # push to single line
    #print('Part 3: Updated: ', name)
    stock_prices.append(name)
len(stock_prices)

for names in stock_prices: 
    print(names)
    
    
list1 = stock_names 
list2 = stock_prices


# create dictionary
dictionary = {'Stock_Names': stock_names, 'Stock_Prices': stock_prices}

## put this together into a dataframe


a = {'Most Active Stocks':stock_names,'Stock_Prices':stock_prices}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df.sample(10).to_markdown())

df.to_csv(r'C:\Users\premd\OneDrive\Desktop\HHA_507_\web-scraping\DATA_CSV_FILE\stock_2.csv')