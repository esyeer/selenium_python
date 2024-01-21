from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

try :
    element = WebDriverWait(driver, 25).until (
    EC.presence_of_element_located((By.NAME, "username")))
    
    driver.find_element(By.NAME, "username").send_keys("myUserName")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("myPass")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Messenger']"))).click()
    # driver.find_element(By.XPATH, "//*[@aria-label='Messenger']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(.,'Not Now')]").click()

    driver.find_element(By.XPATH, "//*[@aria-label='New message']").click()
    
    # Ketikkan Nama Penerima
    time.sleep(3)
    driver.find_element(By.NAME, "queryBox").send_keys("accanq")
    # driver.find_element(By.XPATH, "//*[@placeholder='Search...']").send_keys("accanq")
    time.sleep(3)
    driver.find_element(By.NAME, "ContactSearchResultCheckbox").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x78zum5 x1f6kntn xwhw2v2 xl56j7k x17ydfre x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq']").click()
    time.sleep(3)
    # Tulisan Isi Pesan
    driver.find_element(By.XPATH, "//*[@aria-describedby='Message']").send_keys("coba-coba automated testing kirim pesan ke instagram pake selenium")
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[contains(text(),'Send')]").click()
    time.sleep(5)

    print("BERHASIL")
except TimeoutException:
    print("element tidak ditemukan")    

