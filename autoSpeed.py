from os import pipe
import time
from socket import timeout # it is used to connect a client and a server
from selenium import webdriver # the holy webdriver to control all all the commands
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# print("\n\nHello, welcome to the automated speed scanner:\n\n")

# this must be targeted to the webdriver installation folder
PATH = "D:\Installed_Programs\chromedriver.exe"
driver = webdriver.Chrome(PATH) #storing the webdriver in a variable

driver.get("https://fast.com/") #this time its an custom made website to test web threats.
print("\n\n")

infoLink = driver.find_element_by_id("show-more-details-link")
time.sleep(10)

status = infoLink.is_displayed()

print(status)


if(status ==  True):
    #the speed values be it in 100 or thousands
    speedvalue = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
        (By.ID, 'speed-value')) 
        )
    # print (speedvalue.text)
    #for the speed test units be it in mpbs or kbps acc. to the browser
    speedunits = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
        (By.ID, 'speed-units')) 
        )
    print (speedvalue.text ,speedunits.text)

driver.quit()
