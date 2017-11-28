from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()

zzz=1
url_of_interest='http://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=191&maximumRecords=1&page=192&query=%28gallica%20all%20%22girault%20de%20prangey%22%29&filter=dc.type%20all%20%22image%22'
driver.get(url_of_interest)


csv_file = open('results.csv', 'a')
key_file = open('keys.csv','a')
writer = csv.writer(csv_file, delimiter='#')
key_writer = csv.writer(key_file, delimiter='#')
#writer.writerow(['title', 'subject'])
# Page index used to keep track of where we are.
index = 1
while True:
	try:
		time.sleep(zzz)
		print "Scraping Page number " + str(index)
		index = index + 1

		# Find all the results.
		results = driver.find_elements_by_xpath('//*[@id="searchResultsArea"]/div/div')
#		print results
		for result in results:
			# open details area
			button_path = './/*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[4]/a'
			button = result.find_element_by_xpath(button_path)
			button.click()
			time.sleep(zzz)
			# Now the details area, with its info, should be open to scrape
			
			# Loop through key elements to get the value keys, there are also a variable number of elements
			keys = driver.find_elements_by_xpath('.//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[5]/div/dl/dt')
			keys_lst = []
			for key in keys:
				keys_lst.append(key.find_element_by_xpath('.//b').text.encode('utf-8'))

			# Loop through key elements to get the value keys, there are also a variable number of elements
			values = driver.find_elements_by_xpath('.//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[5]/div/dl/dd')
                        values_lst = []
                        for value in values:
                                values_lst.append(value.find_element_by_xpath('.').text.encode('utf-8'))
			
			extras = driver.find_elements_by_xpath('.//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[5]/div/dl/div')
                        for extra in extras:
                                keys_lst.append(extra.find_element_by_xpath('./dt/b').text.encode('utf-8'))
                                values_lst.append(extra.find_element_by_xpath('./dd/span[1]').text.encode('utf-8'))
			
			

			key_writer.writerow(keys_lst)
			writer.writerow(values_lst)

		# Locate the next button on the page.
		button = driver.find_element_by_xpath('//*[@id="nextResultPage"]')
		button.click()

	except Exception as e:
		print e
		csv_file.close()
		key_file.close()
		driver.close()
		break

