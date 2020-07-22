from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_password_reset_link = (By.PARTIAL_LINK_TEXT, "/password-reset/")

    # login_form = (By.CSS_SELECTOR, "div.login_form")
    login_email_address_form = (By.ID, "id_login-username")
    login_password_form = (By.ID, "id_login-password")
    login_confirm_button = (By.CSS_SELECTOR, "button[name='login_submit']")

    registration_form = (By.CSS_SELECTOR, "div.register_form")
    registration_email_form = (By.ID, "id_registration-email")
    registration_password_form = (By.ID, "id_registration-password1")
    registration_password_confirm_form = (By.ID, "id_registration-password2")
    registration_confirm_button = (By.CSS_SELECTOR, "button[name='registration_submit']")

    success_registration_alert = (By.CSS_SELECTOR, "div.alert.alert-success.fade.in")
