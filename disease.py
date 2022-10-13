import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://wonder.cdc.gov/nndss/static/2022/39/2022-39-table1q.html')
page
#page.text

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')  ### get repo descriptions

# print pretty
print(soup.prettify())


# CREATE DATAFRAME 


repo_name = soup.find_all(id,class_='lbl')
repo_names = []

for item in repo_name:
    print(item.text)
    name = item.text 
    print('Part 1: Raw: ', name)
    
    ## clean name remove upper whitespace or blank space that exist at the top
    name = name.strip()   
    #print('Part 2: Updated: ', name)
    
    ## remove new line, and replace with no spae (whitespace) or remove additional lines that exists and push everything into single line
    name = name.replace('\n','')
    #print('Part 3: Updated: ', name)
    
    ## remove all white space
    name = name.replace(' ','')
    print('Part 4: Updated: ', name)
    
    repo_names.append(name)

len(repo_names)

for names in repo_names:    #  to loop through repo underscore names and just print each of the items that exists within that list
    print(names)
    
len(repo_name)
  
  
# CREATE 2nd Data

repo_count = soup.find_all('td',headers='M3-3')
repo_counts = []

for item in repo_count:
    print(item.text)
    name = item.text 
    print('Part 1: Raw: ', name)
    
    ## clean name remove upper whitespace or blank space that exist at the top
    name = name.strip()   
    #print('Part 2: Updated: ', name)
    
    ## remove new line, and replace with no spae (whitespace) or remove additional lines that exists and push everything into single line
    name = name.replace('\n','')
    #print('Part 3: Updated: ', name)
    
    ## remove all white space
    name = name.replace(' ','')
    print('Part 4: Updated: ', name)
    
    repo_counts.append(name)

len(repo_counts)

for names in repo_counts:    #  to loop through repo underscore names and just print each of the items that exists within that list
    print(names)
    
len(repo_count)
  

# CREATE 3rd Data

repo_count2 = soup.find_all('td',headers='M3-7')
repo_count2s = []

for item in repo_count2:
    print(item.text)
    name = item.text 
    print('Part 1: Raw: ', name)
    
    ## clean name remove upper whitespace or blank space that exist at the top
    name = name.strip()   
    #print('Part 2: Updated: ', name)
    
    ## remove new line, and replace with no spae (whitespace) or remove additional lines that exists and push everything into single line
    name = name.replace('\n','')
    #print('Part 3: Updated: ', name)
    
    ## remove all white space
    name = name.replace(' ','')
    print('Part 4: Updated: ', name)
    
    repo_count2s.append(name)

len(repo_count2s)

for names in repo_count2s:    #  to loop through repo underscore names and just print each of the items that exists within that list
    print(names)
    
len(repo_count2)


###  Create dataset


list1 = repo_names 
list2 = repo_counts
list3 = repo_count2s

# create dictionary
dictionary = {'Reporting Areas': list1, 'Hepatitis B, perinatal infection: Cumulative YTD 2022 counts': list2, 'Hepatitis C, acute: Cumulative YTD 2022 counts': list3}

## put this together into a dataframe

a = {'Reporting Areas': list1, 'Hepatitis B, perinatal infection: Cumulative 2022 year-to-date counts': list2, 'Hepatitis C, acute: Cumulative 2022 year-to-date counts': list3}

df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df.sample(10).to_markdown())
df.to_csv(r'C:\Users\premd\OneDrive\Desktop\HHA_507_\web-scraping\DATA_CSV_FILE\disease_data.csv')