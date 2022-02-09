from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ------------------------------------------------ Create Driver -------------------------------------------
service = Service(executable_path="E:\Softwares\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2772451398&f_AL=true&geoId=92000000&keywords=writer&location=Worldwide")

# ------------------------------------------------ Sign In To LinkedIn -------------------------------------------
sign_in_main_page = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_main_page.click()
user_name = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
user_name.send_keys("eshratisina@gmail.com")
password.send_keys("sinairge1376")
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(3)

# ------------------------------------------------ Apply For The Job -------------------------------------------
apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
apply.click()
phone_number = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2772451398,9,phoneNumber~nationalNumber)"]')
phone_number.send_keys("+995593601624")

# --------------------  Uncomment this part if you really want to apply for the job ----------------------
# submit = driver.find_element(By.XPATH, '//*[@id="ember362"]/span')
# submit.click()
