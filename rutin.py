from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementNotVisibleException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
baseUrl = "https://katalon-demo-cura.herokuapp.com/";					
driver.get(baseUrl)

# driver.get("https://katalon-demo-cura.herokuapp.com/")

# CLick Button "Make Appointment" By.ID
element = driver.find_element(By.ID, "btn-make-appointment")

is_clickable = element.is_enabled()

assert is_clickable, "Element is not clickable"

element.click()
time.sleep(2)

elements = driver.find_elements(By.XPATH, "//section[@id='login']/div/div/div/p")

# Get the element's text
first_element = elements[0]
first_element_text = first_element.text

# Verify if the expected text is present
expected_text = "Please login to make appointment."
assert expected_text in first_element_text, "Expected text not found"
print(first_element_text)
#Input Username and Password By.NAME
driver.find_element(By.NAME, "username").send_keys("John Doe")
driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")
# time.sleep(5)
# Find the button element
# tombol = driver.find_element(By.ID, "btn-login")

#verify tombol login bisa di klik
try:
    tombol = driver.find_element(By.ID, "btn-login")
    if not tombol.is_enabled():
        raise AssertionError("Element is not enabled")

    tombol.click()
except (ElementNotVisibleException, ElementClickInterceptedException, StaleElementReferenceException):
    assert False, "Element is not clickable or visible"

#verify setelah login
elements = driver.find_elements(By.XPATH, "//section[@id='appointment']/div/div/div/h2")

expected_text = "Make Appointment"
text_found = False
for element in elements:
    if expected_text in element.text:
        text_found = True
        break

assert text_found, "Expected text not found"