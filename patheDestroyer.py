from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome("./usr/bin/chromedriver")
driver.set_window_size(1920, 1080)
driver.set_page_load_timeout(100)

print("Pathe destroyer is starting")
driver.get("http://s.cinemaspathegaumont.com/#/C3132S50381/booking")

def find(driver):
    element = driver.find_elements_by_id("seatIdF4")
    if element:
        return element
    else:
        return False

def addPlace(placeNM):
    element = WebDriverWait(driver, 30).until(find)
    element = driver.find_element_by_xpath(placeNM)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(4)


print("One Seat Blocked")
addPlace('//*[@id="seatIdF4"]')
print("Two Seats Blocked")
addPlace('//*[@id="seatIdF3"]')

print("Three Seats Blocked")

addPlace('//*[@id="seatIdF5"]')
print("Four Seats Blocked")
addPlace('//*[@id="seatIdF1"]')
print("Five Seats Blocked")
addPlace('//*[@id="seatIdF2"]')


def find1(driver):
    element = driver.find_elements_by_xpath("/html/body/cgp-front-app/section/div[1]/div[4]/div[8]/div[2]")
    if element:
        return element
    else:
        return False

print("Going to checkout")
element = WebDriverWait(driver, 30).until(find1)
element = driver.find_element_by_xpath("/html/body/cgp-front-app/section/div[1]/div[4]/div[8]/div[2]/a")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)


def find2(driver):
    element = driver.find_elements_by_xpath(
        "/html/body/cgp-front-app/section/div[1]/div[3]/div[1]/div[1]/div[1]/div/div[2]/button")
    if element:
        return element
    else:
        return False


element = WebDriverWait(driver, 30).until(find2)
element = driver.find_element_by_xpath(
    "/html/body/cgp-front-app/section/div[1]/div[3]/div[1]/div[1]/div[1]/div/div[2]/button")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)


def find3(driver):
    element = driver.find_elements_by_xpath('//*[@id="popin-ajout-carte-cinepass"]/div[2]/div/div[1]/div/a')
    if element:
        return element
    else:
        return False

element = WebDriverWait(driver, 30).until(find3)
element = driver.find_element_by_xpath('//*[@id="popin-ajout-carte-cinepass"]/div[2]/div/div[1]/div/a')
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
def find4(driver):
    element = driver.find_elements_by_xpath("/html/body/section/div[2]/div/a[2]")
    if element:
        return element
    else:
        return False
element = WebDriverWait(driver, 30).until(find4)
element = driver.find_element_by_xpath("/html/body/section/div[2]/div/a[2]")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

print("Pathe destroyer will run again in 10 minutes")
driver.quit()