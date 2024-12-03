from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

username = os.getenv("usr")
password = os.getenv("password")
print(f"Username: {username}")
print(f"Password: {password}")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://swarnaislam2000.infy.uk/wp-admin/")
# get the username and password from the .env file
# Login phase
driver.find_element(By.ID, "user_login").send_keys(username)

driver.find_element(By.ID, "user_pass").send_keys(password)
driver.find_element(By.ID, "wp-submit").click()
time.sleep(5)
# click the plugins button
driver.find_element(By.CSS_SELECTOR, ".wp-menu-image.dashicons-before.dashicons-admin-plugins").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Installed Plugins']").click()
# scroll top to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# check the darkmode active or deactibe
try:
    wp_dark_mode_element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//tr[@data-slug='wp-dark-mode']")))
    print("WP dark mode is installed.")
except:
    print("WP Dark Mode is not installed. Installing...")
    # install the plugin
    driver.find_element(By.CSS_SELECTOR, ".wp-menu-image.dashicons-before.dashicons-admin-plugins").click()
    add_new_pagins = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='plugin-install.php']")))
    add_new_pagins.click()
    search = driver.find_element(By.ID, "search-plugins").click()
    search.send_keys("WP Dark Mode").submit()
    time.sleep(5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Install WP Dark Mode now']"))).click()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='Activate WP Dark Mode']").click()
    time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".wp-menu-image.dashicons-before.dashicons-admin-plugins").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Installed Plugins']").click()
try:
    wp_dark_mode = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//tr[@data-slug='wp-dark-mode']")))
    active_link = wp_dark_mode.find_element(By.XPATH, "//a[@id='deactivate-wp-dark-mode']")
    if active_link:
        print("WP Dark Mode is already activate.")
    else:
        print("WP Dark Mode is not activated. Activating...")
        time.sleep(10)
        # jate kono unexpected accur na hoy holeo jate handle korte pare
        try:
            submit_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "activate-akismet"))
            )
            submit_button.click()
            print("Submit button clicked successfully.")
        except Exception as e:
            print(f"Failed to click submit button: {e}")
            time.sleep(3)
    print("swarna")
   
except Exception as e:
    print(f"Failed to install or activate WP Dark Mode: {e}")      
# wp dark mode panel 
try:
    driver.find_element(By.CSS_SELECTOR, "#toplevel_page_wp-dark-mode > a > div.wp-menu-name.wp-dark-mode-ignore").click()    
    print("now wp dark mode panel")
except Exception as e:
    print(f"Failed to open WP Dark Mode panel: {e}")
    
try:
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/a[2]'))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='w-5 h-5 flex rounded-full mt-0.5 ml-0.5 transition duration-100 wp-dark-mode-ignore border-4 border-white bg-slate-200 wp-dark-mode-ignore']"))).click()
    print("Admin panel dark mode is on")
except Exception as e:
    print(f"Failed to activate admin panel dark mode: {e}")
# validate the admin wp_dark_mode is working

try:
    validate = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(1)")))
    valid_wp_dark_mode = driver.find_element(By.CSS_SELECTOR, "#wp-dark-mode-admin > div > div > div > div.main-content > div.main-content-body > section:nth-child(1) > div.rounded.text-base.flex.flex-col.gap-3.bg-transparent.gap-5 > div:nth-child(1) > label > div.w-auto.h-6.flex.items-center.justify-center > div")
    if valid_wp_dark_mode:     
        print("validation : WP Dark Mode is working as expected.") 
    else:
        print("validation : WP Dark Mode is not working as expected.")
except Exception as e:
    print(f"Failed to validate: {e}")

# navigate the wp dark mode 
driver.find_element(By.CSS_SELECTOR, "#toplevel_page_wp-dark-mode > a > div.wp-menu-name.wp-dark-mode-ignore").click()    

# customizatio -> switch settings -> floating switch style
try:
    driver.find_element(By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[1]/div[2]/div[2]/div/div/div/h4').click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Switch Settings']").click()
    time.sleep(5)
# click floating switch style
    # element = driver.find_element(By.CSS_SELECTOR, "#wp-dark-mode-admin > div > div > div > div.main-content > div.main-content-body > div > section > div.flex.flex-col.gap-6 > div > div.rounded.text-base.flex.flex-col.gap-3.bg-transparent.gap-5 > div.rounded.text-base.flex.flex-col.gap-3.bg-white.py-5.px-6.gap-6 > div.rounded.text-base.flex.flex-col.gap-3.bg-transparent > div.flex.flex-col.gap-1.text-base.leading-6.text-black.font-medium")
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    
    driver.find_element(By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[2]')
    driver.find_element(By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]').click()
# save the change
    driver.find_element(By.CSS_SELECTOR, "button[class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']").click()
    print("Switch Floating Switch Style")
except Exception as e:
    print(f"Failed to switch Floating Switch Style: {e}")
# customizatio -> switch settings -> cutomization switch size & scale 220
try:
    element = driver.find_element(By.CSS_SELECTOR, "#wp-dark-mode-admin > div > div > div > div.main-content > div.main-content-body > div > section > div.flex.flex-col.gap-6 > div > div.rounded.text-base.flex.flex-col.gap-3.bg-transparent.gap-5 > div.rounded.text-base.flex.flex-col.gap-3.bg-transparent > div")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(By.XPATH, "//body/div[@id='wpwrap']/div[@id='wpcontent']/div[@id='wpbody']/div[@id='wpbody-content']/div[@id='wp-dark-mode-admin']/div[@class='relative']/div[@class='relative']/div[@class='app-wrapper']/div[@class='main-content']/div[@class='main-content-body']/div[@class='rounded text-base flex flex-col gap-3 bg-transparent gap-5']/section[@class='flex flex-col gap-6 w-full']/div[@class='flex flex-col gap-6']/div[@class='rounded text-base flex flex-col gap-3 bg-transparent gap-5']/div[@class='rounded text-base flex flex-col gap-3 bg-transparent gap-5']/div[@class='rounded text-base flex flex-col gap-3 bg-white py-5 px-6 gap-8']/div[@class='flex gap-6 justify-between flex-wrap']/div[@class='flex flex-col w-fit gap-6']/div[1]")
    driver.find_element(By.XPATH, "//div[@class='cursor-pointer flex items-center gap-2 py-2 transition duration-75 px-3.5 text-base font-normal leading-6 rounded-lg bg-gray-100 hover:bg-gray-200']//span[contains(text(),'Custom')]").click()
    
    slider = driver.find_element(By.XPATH, "//input[@type='range']")
    action = ActionChains(driver)
    action.click_and_hold(slider).move_by_offset(47, 0).release().perform()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button[class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']").click()
    print("Customize Switch Size & Scale to 220")
except Exception as e:
    print(f"failed customizing switch size & scale: {e}")
    
# change the Switch Position to left
try:
    
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']").click()
    print("Change Switch Position to Left")
    time.sleep(2)
except Exception as e:
    print(f"failed changing switch position: {e}")
    
# disable key shortcut from accessibility settings
try:
    print("Disabling Key Shortcut from Accessibility Settings")
    driver.find_element(By.XPATH, "//body/div/div/div[@role='main']/div/div/div/div/div/div/div/div[3]/div[1]/div[1]")
    driver.find_element(By.XPATH, "//body/div/div/div[@role='main']/div/div/div/div/div/div/div/div//*[name()='svg']").click()
    try:
        accessibility_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Accessibility']")))
        accessibility_link.click()
        print("Accessibility Settings found")
    except:
        print("Accessibility link not found")
    # driver.find_element(By.XPATH, "//a[normalize-space()='Accessibility']").click()
    element = driver.find_element(By.CSS_SELECTOR, "div[class='main-content'] div:nth-child(5)")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(3)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rounded text-base flex flex-col gap-3 bg-white py-5 px-6 gap-5']")))
    # driver.find_element(By.XPATH, "//div[@class='rounded text-base flex flex-col gap-3 bg-white py-5 px-6 gap-5']")
    WebDriverWait(driver, 30).until(EC.element_located_to_be_selected((By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[6]/div[1]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='w-5 h-5 flex rounded-full mt-0.5 ml-0.5 transition duration-100 wp-dark-mode-ignore translate-x-4 border-none bg-[#fff] wp-dark-mode-ignore']"))).click()
    print("Disable Key Shortcut from Accessibility Settings")
    time.sleep(2)
except Exception as e:
    print("Exception occurred while disabling key shortcut: ", str(e))
    
# customization-> siteanimations -> enable page transitionanimation
try:
    driver.find_element(By.XPATH, "//body/div/div/div[@role='main']/div/div/div/div/div/div/div/div[3]/div[1]/div[1]")
    driver.find_element(By.XPATH, "//body/div/div/div[@role='main']/div/div/div/div/div/div/div/div//*[name()='svg']").click()

    driver.find_element(By.XPATH, "//a[normalize-space()='Site Animation']").click()
    time.sleep(3)
    # box xpath
    driver.execute_script("window.scrollTo(0, 0);")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex text-base w-full rounded flex-col py-5 px-6 bg-white']")))
    time.sleep(3)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#wp-dark-mode-admin > div > div > div > div.main-content > div.main-content-body > div > div > div:nth-child(1) > div > div > div > label > div.w-auto.h-6.flex.items-center.justify-center > div > span"))).click()
    print("Enable Page Transition Animation")
    time.sleep(3)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div')))
    dropdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)")))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    driver.execute_script("arguments[0].click();", dropdown)
    
    # driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)").click()
    # save change 
    driver.find_element(By.CSS_SELECTOR, "button[class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']").click()
    print("change the animation effect successfully ")
    time.sleep(3)
except Exception as e:
    print(f"failed to enable page transition An error occurred: {e}")
# switch the user panel   
new_tab = "http://swarnaislam2000.infy.uk/?i=1"

driver.switch_to.new_window()
driver.get(new_tab)
try:
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div")))
    print("Dark mode switch found")
    driver.find_element(By.XPATH, "//html")
    body_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "wp-dark-mode-active")))
    if body_element:
        print("Validate : Dark mode working from the front end")
    else:
        print(" Dark mode not working from the front end")
except Exception as e:
    print(f"Failed to validate Dark mode: {e}")
    
time.sleep(3)

driver.quit()
