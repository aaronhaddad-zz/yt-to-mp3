from selenium import webdriver
import time


print("Enter youtube URL: ",end=" ")
url_user=input()

#The line below is used to import the webdriver. You can replace chrome by your favourite web browser. Check the readme for more info!
driver=webdriver.Chrome()
driver.get("https://ytmp3.cc/en13/")

urlBar=driver.find_element_by_xpath("//*[@id='input']")
urlBar.send_keys(url_user)

driver.find_element_by_xpath("//*[@id='submit']").click()

#I made this 10 second pause, in order for the converter to process longer videos, howerver you can reduce the hold to a second or two. Check the readme for more info!
time.sleep(10)
driver.find_element_by_xpath("//*[@id='buttons']/a[1]").click()
driver.close()