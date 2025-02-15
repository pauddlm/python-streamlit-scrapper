from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def navigate_to_tests(driver):

    # Find the "Test" element to hover the mouse over it
    test_element = driver.find_element(By.ID, 'mnu1')

    # Find the "Permiso B" link in the submenu
    permiso_b_link = driver.find_element(By.XPATH, "//a[@title='test permiso B']")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Hover the mouse over the "Test" element and click on "Permiso B"
    actions.move_to_element(test_element).move_to_element(permiso_b_link).click().perform()

    # Wait a bit to ensure the "Permiso B" page has loaded
    time.sleep(1)

    test_dgt_element = driver.find_element(By.XPATH, "//a[@title='Test permiso B de la DGT']")
    # Hover the mouse over the "Test" element and click on "Permiso B"
    actions.move_to_element(test_dgt_element).click().perform()
