from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# ------------------------------------------------ Create Driver -------------------------------------------
service = Service(executable_path="E:\Softwares\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2807783708&f_"
           "AL=true&geoId=92000000&keywords=writer&location=Worldwide")

# ------------------------------------------------ Sign In To LinkedIn -------------------------------------------
sign_in_main_page = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_main_page.click()
user_name = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
user_name.send_keys("eshratisina@gmail.com")
password.send_keys("sinairge1376")
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(1)

# ------------------------------------------------ Apply For All The Jobs -------------------------------------------
jobs = driver.find_elements(By.CLASS_NAME, 'job-card-list__title')
for job in jobs:
    job.click()
    time.sleep(2)
    apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    apply.click()
    time.sleep(2)

    # ---------------------------------- Reject Offers That Are Not Simple One Step ---------------------------------
    if driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary .artdeco-button__text').text == "Next":
        close = driver.find_element(By.CLASS_NAME, 'artdeco-button__icon')
        close.click()
        time.sleep(2)
        discard = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar '
                                                       '.artdeco-button--secondary .artdeco-button__text ')
        discard.click()

        # ---------------------------------- Submit Offers That Are Simple One Step -----------------------------
    else:
        # ----------- Because this program is only practical, We don't actually hit the submit button. -------------
        print("submit application")
        close = driver.find_element(By.CLASS_NAME, 'artdeco-button__icon')
        close.click()
        time.sleep(2)
        discard = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar '
                                                       '.artdeco-button--secondary .artdeco-button__text ')
        discard.click()

        # ---------------- Use the code below if you intend to submit your application --------------------
        # submit = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary .artdeco-button__text')
        # submit.click()

driver.quit()
