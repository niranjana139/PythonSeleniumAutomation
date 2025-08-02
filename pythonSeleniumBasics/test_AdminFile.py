from pages.AdminPage import AdminPage
from pages.LoginPage import Login


def test_verify_search(browserinstance):
    driver = browserinstance
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    driver.maximize_window()
    login = Login(driver)
    login.validateLogin()

    # Initialize AdminPage object
    admin_page = AdminPage(driver)
    isDisplayed=admin_page.performSearch()
    assert isDisplayed is True
    #assert isDisplayed is False
