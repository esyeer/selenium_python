from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "confirmButton").click()
time.sleep(5)

# allert.switch_to_allert
# alert = Alert(driver)
try:
    # Try to switch to the alert
    alert = Alert(driver)
    alert_text = alert.text
    # If successful, the alert is present
    print(alert.text, "Alert Is Displayed")

    # Perform actions with the alert (e.g., accept, dismiss)
    # alert.accept()  # Uncomment this line if you want to accept the alert
    # alert.dismiss()  # Uncomment this line if you want to dismiss the alert

except NoAlertPresentException:
    # If NoAlertPresentException is thrown, it means there is no alert
    print("No alert found on the page.")

alert.dismiss()
print("You clicked Cancel")

# Close the browser when done
driver.quit()

