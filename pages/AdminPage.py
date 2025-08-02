from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators for Admin Page elements
        self.tile_locator = (By.XPATH,
                             "//a[contains(@class, 'small-box-footer') and @href='https://groceryapp.uniqassosiates.com/admin/list-admin']")
        self.new_button_locator = (By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.add_name_locator = (By.ID, "username")
        self.add_password_locator = (By.ID, "password")
        self.user_type_locator = (By.ID, "user_type")
        self.save_button_locator = (By.XPATH, "//button[@name='Create']")

        self.search_locator = (By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.username_locator = (By.ID, "un")
        self.user_type_drop_locator = (By.ID, "ut")
        self.search_button_locator = (By.XPATH, "//button[@name='Search']")

        self.reset_button_locator = (By.XPATH, "//a[@class='btn btn-rounded btn-warning']")

        # Implicit wait for all elements
        self.driver.implicitly_wait(10)

    def click_tile(self):
        """Click on the tile to navigate"""
        self.driver.find_element(*self.tile_locator).click()

    def add_data_and_click_save(self, name, password, user_type_value):
        """Click on tile, open new form, and save user"""
        self.click_tile()  # Navigate to the admin page
        self.driver.find_element(*self.new_button_locator).click()

        # Fill out the form
        self.driver.find_element(*self.add_name_locator).send_keys(name)
        self.driver.find_element(*self.add_password_locator).send_keys(password)

        select = Select(self.driver.find_element(*self.user_type_locator))
        select.select_by_visible_text(user_type_value)

        self.driver.find_element(*self.save_button_locator).click()

    def is_search_button_displayed(self):
        """Check if the search button is displayed"""
        return self.driver.find_element(*self.search_button_locator).is_displayed()

    def search_user(self, name, user_type):
        """Search for a user by name and user type"""
        self.driver.find_element(*self.search_locator).click()

        self.driver.find_element(*self.username_locator).send_keys(name)

        select = Select(self.driver.find_element(*self.user_type_drop_locator))
        select.select_by_visible_text(user_type)

        self.driver.find_element(*self.search_button_locator).click()

    def is_reset_button_displayed(self):
        """Check if the reset button is displayed"""
        return self.driver.find_element(*self.reset_button_locator).is_displayed()

    def reset(self):
        """Click on the reset button to clear fields"""
        self.driver.find_element(*self.reset_button_locator).click()

