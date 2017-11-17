from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#driver = webdriver.Chrome()
driver = webdriver.Chrome()

zzz=3
url_of_interest='http://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=1&page=1&query=%28gallica%20all%20%22girault%20de%20prangey%22%29&filter=dc.type%20all%20%22image%22'
driver.get(url_of_interest)


csv_file = open('results.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['title', 'subject'])
# Page index used to keep track of where we are.
index = 1
while True:
	try:
		time.sleep(zzz)
		print "Scraping Page number " + str(index)
		index = index + 1

		# Find all the results.
		results = driver.find_elements_by_xpath('//*[@id="searchResultsArea"]/div/div')
	#	results = driver.find_elements_by_xpath('//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[3]')
#		print results
		inner_index=1
		for result in results:
			print 'back again'

			# open details area
			button_path = './/*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[3]/a'
			button = result.find_element_by_xpath(button_path)
			# Scroll into view
#			driver.execute_script("return arguments[0].scrollIntoView(true);", button_path)
		#	button = result.find_element_by_xpath('.//div[@class="main-infos"]//a[2]')
#			print 'after button definition'
			button.click()
#			print 'after click'
			time.sleep(3)
			# Now the details area, with its info, should be open to scrape

			result_dict = {}
		#	title_xpath='.//*[@id="notice-details-1"]/div/dl/dd[1]'
		#	subject_xpath='.//*[@id="notice-details-1"]/div/dl/dd[12]'
			title_xpath='.//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[4]//dl/dd[1]'
			subject_xpath='.//*[@id="contenu"]/div[2]/div[1]/div/div[1]/div[4]//dl/dd[12]'
#			print 'after definitions'
			title = result.find_element_by_xpath(title_xpath).text.encode('utf-8')
#			print 'here 1'	
			subject = result.find_element_by_xpath(subject_xpath).text.encode('utf-8')
#			print 'here 2'
			result_dict['title'] = title
			result_dict['subject'] = subject
   			writer.writerow(result_dict.values())
			print 'writing'
			print title, subject
			#script = "window.scrollTo(0, document.body.scrollHeight/%d);" % (50.0/inner_index)
#			script = "window.scrollTo(0, document.body.scrollHeight);"
#			driver.execute_script(script)
#			inner_index = inner_index + 1


		# Locate the next button on the page.
		button = driver.find_element_by_xpath('//*[@id="nextResultPage"]')
		button.click()
		index = 1                

	except Exception as e:
		print e
		csv_file.close()
		driver.close()
		break

