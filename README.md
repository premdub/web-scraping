# web-scraping
1. Create a new github repo called 'web-scraping' 

2. Using BS4, find at least 2 websites that you want to scrap data from - provide that code within a .py file  

3. In the code, for each website - create at least one dataframe that has structured data 

4. Save each of the dataframes as separate .csv files into a "/data" folder within your repo - be sure to include the .csv files within your repo (make sure they are small, < 25mb) 

5. Include a markdown file in the repo which includes instructions (e.g., what are the required python packages to run this, your approach for scrapping the data - the div/classes/css tags you found to extract the information)
   
     -  The required python packages to run are: $pip install beautifulsoup4                                                          

    - The approach for scrapping data is to discover Nationally Notifiable Infectious Diseases and Conditions, United States Tables from CDC website.  
        -Cumulative 2022 year-to-date counts for Hepatitis B, perinatal infection & Hepatitis C, acute 

   -  Another approch for scrapping stock data is to finding asto most popular and most active stocks from webull website. The 2-separate-py.file was created for most          active stocks and most popular stocks with pertinents data related to each kind of stock. 

    - The tags to extrat the information, for example, "div", "p", and "span".  However  I encountered error on "span" and "csr" tag.  It would not give any output on 
    these two tags.    
  
