from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def login(driver, username, password):

    try:
        # Wait for the elements to be present (you can use WebDriverWait if necessary)
        time.sleep(1)

        # Reject cookies in the popup window
        try:
            non_accept_button = driver.find_element(By.XPATH, "//button/span[text()='NO ACEPTO']")
            non_accept_button.click()
            print("Cookies policy has been rejected.")
        except Exception as e:
            print("Could not find the accept cookies button:", e)

        # Locate and fill the Email/Username field
        username_field = driver.find_element(By.ID, 'e_ini')
        username_field.send_keys(username)

        # Locate and fill the Password field
        password_field = driver.find_element(By.ID, 'contra')
        password_field.send_keys(password)

        # Submit the form (you can click the button or use submit)
        password_field.send_keys(Keys.RETURN)

        # Wait to see the result
        time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")