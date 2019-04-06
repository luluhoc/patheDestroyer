from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
display = Display(visible=0, size=(1920, 1080))
display.start()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
#choose your seats
seat = ['//*[@id="seatIdE15"]', '//*[@id="seatIdE16"]', '//*[@id="seatIdE17"]', '//*[@id="seatIdE18"]', '//*[@id="seatIdE19"]', '//*[@id="seatIdE20"]']
#Link to movie booking
bookingLink = "http://s.cinemaspathegaumont.com/#/C3132S50381/booking"


driver.set_page_load_timeout(100)
print("Pathe destroyer is starting")
driver.get(bookingLink)

def find(driver):
    element = driver.find_elements_by_id("seatIdF4")
    if element:
        return element
    else:
        return False

def addPlace(placeNM):
    element = WebDriverWait(driver, 10).until(find)
    element = driver.find_element_by_xpath(placeNM)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)


print("One Seat Blocked")
addPlace(seat[0])
print("Two Seats Blocked")
addPlace(seat[1])
print("Three Seats Blocked")
addPlace(seat[2])
print("Four Seats Blocked")
addPlace(seat[3])
print("Five Seats Blocked")
addPlace(seat[4])
print("Six Seats Blocked")
addPlace(seat[5])

element = driver.find_element_by_xpath("/html/body/cgp-front-app/section/div[1]/div[4]/div[8]/div[2]/a")
print("Going to checkout")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

element = driver.find_element_by_xpath("/html/body/cgp-front-app/section/div[1]/div[3]/div[1]/div[1]/div[1]/div/div[2]/button")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

element = driver.find_element_by_xpath('//*[@id="popin-ajout-carte-cinepass"]/div[2]/div/div[1]/div/a')
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

element = driver.find_element_by_xpath("/html/body/section/div[2]/div/a[2]")
driver.execute_script("arguments[0].click();", element)
print("Pathe destroyer will run again in 10 minutes")
driver.quit()



