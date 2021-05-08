from os import pipe
import time
from socket import timeout # it is used to connect a client and a server
from selenium import webdriver # the holy webdriver to control all all the commands
from selenium.webdriver.common import alert
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
time.sleep(30)

status = infoLink.is_displayed()

print(status)

'''
link = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
link.click()'''
if(status ==  True):

    speedvalue = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
        (By.ID, 'speed-value')) 
        )
    print (speedvalue.text)


# info_link = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#     (By.XPATH, html/body/div'//div[2]/div[1]/div[4]/div[1]/a')) 
#     )

# info_link.click()
# time.sleep(30)

driver.quit()
