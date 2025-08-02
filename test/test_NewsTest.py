import pytest
from selenium.webdriver.chrome import webdriver

from pages import LoginPage
from pages import NewsPage
from utilities.ExcelUtility import ExcelUtility

class TestNewsTest:

    def test_verify_add_news(login_page, news_page, username_column, password_column):
        """Test to verify news addition."""
        excelUtility=ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")



        #ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data( 3,1,"LoginPage")
        password_value = excelUtility.get_string_data(3,2,"LoginPage")


    # Login
        login_page.enter_user_name_on_username_field(username_value)
        login_page.enter_password_on_password_field(password_value)
        login_page.click_on_signin_button()

        # Add News
        news_page.add_news()

        # Assert Alert is displayed
        assert news_page.is_alert_displayed(), "Alert is not displayed for adding news"

    @pytest.mark.smoke
    @pytest.mark.parametrize("username_column, password_column", [(1, 0), (1, 1)])  # Parametrize to fetch login details
    def test_verify_reset(login_page, news_page, username_column, password_column):
        """Test to verify reset functionality."""
        excelUtility=ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")



        #ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data( 2,1,"LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")

        # Login
        login_page.enter_user_name_on_username_field(username_value)
        login_page.enter_password_on_password_field(password_value)
        login_page.click_on_signin_button()

        # Verify Reset functionality
        news_page.click_tile()
        is_visible = news_page.is_reset_button_displayed()
        news_page.reset_page()
        assert is_visible, "Reset button is not visible"


    @pytest.mark.parametrize("username_column, password_column", [(1, 0), (1, 1)])  # Parametrize to fetch login details
    def test_verify_search_news(self,login_page, news_page, username_column, password_column):
        """Test to verify news search functionality."""
        username_value = ExcelUtility.get_string_data(self, username_column, 0, "LoginPage")
        password_value = ExcelUtility.get_string_data(self,password_column, 1, "LoginPage")

        # Login
        login_page.enter_user_name_on_username_field(username_value)
        login_page.enter_password_on_password_field(password_value)
        login_page.click_on_signin_button()

        # Search News
        news_page.click_tile()
        is_displayed = news_page.is_search_button_displayed()
        news_page.search_news()

        # Assert Search Button is visible
        assert is_displayed, "Search button is not visible"
