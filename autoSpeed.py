from os import pipe
import time
from socket import timeout # it is used to connect a client and a server
from selenium import webdriver # the holy webdriver to control all all the commands
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# print("\n\nHello, welcome to the automated speed scanner:\n\n")
''' abhishek kumar(abhi00o7)
'''
# this must be targeted to the webdriver installation folder
PATH = "D:\Installed_Programs\chromedriver.exe"
driver = webdriver.Chrome(PATH) #storing the webdriver in a variable

def autospeedtest(url):

    driver.get(url) #this time its an custom made website to test web threats.
    print("\n\n")

    wait = WebDriverWait(driver, 40)
    try:
        infoLink = wait.until(
                EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[1]/div[4]/div[1]/a')) 
                )

        status = infoLink.is_displayed()

        #CHECK THE STATUS FOR PEACE OF MIND
        # print(status)


        if(status ==  True):
            #the speed values be it in 100 or thousands
            speedvalue = wait.until(
                EC.presence_of_element_located(
                (By.ID, 'speed-value')) 
                )

            #for the speed test units be it in Mpbs or Kbps acc. to the browser
            speedunits = wait.until(
                EC.presence_of_element_located(
                (By.ID, 'speed-units')) 
                )
            print("Your connection speed is :")
            print (speedvalue.text ,speedunits.text)

        # driver.quit()

    except :
        print("You DO NOT have a working internet connection.")
        # driver.quit()

url = "https://fast.com/"

# for index in range(15):
#     print("test: ", index+1)
#     autospeedtest(url)
    
def main():

    autospeedtest(url)
    #closing options
    # driver.close() #to close just the current tab of the browser
    driver.quit()   #to completely force close the browser

if __name__ == '__main__':
    main()