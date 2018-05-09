# scraping_bnfGallica
Selenium script to scrape dePrangey photos and relevant info from http://gallica.bnf.fr

Scrapes all the information from a bunch of photos. Requires Selenium because using scrapy didn't work. Needed to actually interact with
the website to make the information available. 

Scrapes all the data into a pandas dataframe then writes it to a delimited text file. 
