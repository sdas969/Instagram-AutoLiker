from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
username=input("Insta Username: ")
pwd=getpass.getpass("Insta Password: ")
id1=input("Insta ID: ")
n1=int(input("Enter no of posts to like (0 for all posts): "))
driver=webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.instagram.com/")
time.sleep(2)
a=driver.find_element_by_name("username")
a.send_keys(username)
a=driver.find_element_by_name("password")
a.send_keys(pwd)
a.send_keys(Keys.RETURN)
time.sleep(3)
a=driver.find_element_by_class_name("aOOlW.HoLwm ")
a.click()
a=driver.find_element_by_class_name("XTCLo.x3qfX")
a.send_keys(id1)
time.sleep(3)
a=driver.find_elements_by_class_name("Ap253")[0]
a.click()
time.sleep(4)
a=driver.find_elements_by_class_name("g47SY ")[0]
n=int((a.text).replace(',',''))
if (n1>n or n1==0):
    n1=n
time.sleep(3)
a=driver.find_element_by_class_name("eLAPa")
a.click()
time.sleep(3)
for i in range(int(n1)):
    a=driver.find_elements_by_class_name("wpO6b ")[1]
    a.click()
    if (i<(int(n1)-1)):
        a=driver.find_element_by_class_name("_65Bje.coreSpriteRightPaginationArrow")
        a.click()
        time.sleep(4)
a=driver.find_element_by_class_name("Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG")
a.click()
a=driver.find_element_by_class_name("_2dbep.qNELH.kIKUG")
a.click()
time.sleep(2)
a=driver.find_elements_by_class_name("_8-yf5 ")[0]
a.click()
time.sleep(1)
a=driver.find_elements_by_class_name("aOOlW.HoLwm ")[8]
a.click()
