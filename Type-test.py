from bs4 import BeautifulSoup
from selenium import webdriver 
import re
import time

#This program completes the typing test on live-chat.com

url = "https://www.livechat.com/typing-speed-test/"


driver = webdriver.Firefox()
driver.get(url)

clickapp = driver.find_element_by_class_name("input-wrapper")
clickapp.click()

ta = time.time()
cnt = time.time()+62
#the test is 1 minute long
while cnt > ta:
	html = driver.execute_script("return document.documentElement.outerHTML")
	sel_soup = BeautifulSoup(html,"html.parser")
	soup= str(sel_soup.findAll("span",attrs= {"data-reactid":".0.2.0.0.$=12.0.$=10.1.0.$0"}))
	wordlist = re.findall('\$0\">(\w+)</',soup)
	try:
		word = wordlist[0]
	except IndexError:
		continue
	typeapp = driver.find_element_by_id("test-input")
	typeapp.send_keys(word + " ")
	ta = time.time()
	time.sleep(0.15)
#seems I need to add the sleep method, otherwise the browser freezes misteriously
