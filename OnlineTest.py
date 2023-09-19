import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
#
edge_options = Options()
edge_options.add_argument('--disable-notifications')

driver=webdriver.Edge(options=edge_options)

driver.get("https://www.bt.com/")
driver.maximize_window()

time.sleep(5)
#Close accept Cookie pop-up if it appears
try:
    accept_cookie_button = driver.find_element(By.XPATH, "//a[text()='Accept all cookies']")
    accept_cookie_button.click()
except:
    pass

#Hover to Mobile menu
mobile=driver.find_element(By.XPATH,"(//span[text()='Mobile'])[1]")
ActionChains(driver).move_to_element(mobile).perform()


# Click on "Mobile phones"
mobile_phones = driver.find_element(By.LINK_TEXT,"Mobile phones")
mobile_phones.click()

# Verify the numbers of banners present below “See Handset details” should not be less than 3
banners = driver.find_elements(By.XPATH, "//a[@class='bt-btn bt-btn-primary mt-2 mb-12']")
if len(banners) >= 3:
    print("Number of banners is greater than or equal to 3.")
else:
    print("Number of banners is less than 3.")


# Scroll down and click View SIM only deals
sim_only_deals = driver.find_element(By.XPATH, "//a[@class='bt-btn bt-btn-primary']")
driver.execute_script("arguments[0].scrollIntoView(true);", sim_only_deals)
sim_only_deals.click()

# Validate the title for the new page
new_page_title = driver.title
if "SIM Only Deals" in new_page_title:
    print("Title validation passed: " + new_page_title)
else:
    print("Title validation failed: " + new_page_title)

# Validate “30% off and double data” was 125GB 250GB Essential Plan, was £27 £18.90 per month
plan_info = driver.find_element(By.XPATH,"//button[normalize-space()='125GB']")
check_elements = driver.find_elements(By.XPATH,"(//span[text()='Essential Plan']/preceding-sibling::div[text()='250GB'])[2]/parent::div/following-sibling::div/div/sub/text()")
prices=[]
for check in check_elements:
    price =check.text
    prices.__add__(price)


if "30% off and double data" in prices and "125GB 250GB Essential Plan, was £27 £18.90 per month" in prices:
    print("Plan info validation passed: " + prices)
else:
    print("Plan info validation failed: " + prices)

# Close the browser and exit
driver.quit()




