from selenium.webdriver.common.by import By
from .base_page import BasePage
from test_classes.helpers.locator import Locator

class PaymentMethodPage(BasePage):
    add_payment_method_link_locator = Locator(by=By.XPATH, value="//a[@href='http://staging.shopping.beeyor.com/my-account/add-payment-method/']")

    credit_debit_card_iframe_locator = Locator(by=By.XPATH,value="///iframe[@name='__privateStripeFrame1704']")
    card_number_field_locator = Locator(by=By.XPATH, value="//input[@id='Field-numberInput']")
    expiration_date_field_locator = Locator(by=By.XPATH, value="//input[@id='Field-expiryInput']")
    cvc_field_locator = Locator(by=By.XPATH, value="//input[@id='Field-cvcInput']")
    zip_code_field_locator = Locator(by=By.XPATH, value="//input[@id='Field-postalCodeInput']")
    success_message_locator = Locator(by=By.LINK_TEXT, value='Payment method successfully added.')
    payment_methods_link_locator = Locator(by=By.XPATH, value="//a[@href='http://staging.shopping.beeyor.com/my-account/payment-methods/']")

    def wait_for_credit_debit_card_page_to_load(self):
        self.wait_until_element_is_visible(self.credit_debit_card_iframe_locator, timeout=10)

    def click_on_payment_methods(self):
        self.click(self.payment_methods_link_locator)

    def switch_to_iframe(self):
        iframe = self.wait_until_element_is_visible(self.credit_debit_card_iframe_locator,timeout=10)
        self.driver.switch_to.frame(iframe)
        self.driver.switch_to.default_content()

    def add_card_number(self, credit_card_number, expiration_date, cvc, zip_code):
        #card number
        self.switch_to_iframe()
        self.input(self.card_number_field_locator, credit_card_number)
        self.driver.switch_to.default_content()

        #expiration date
        self.switch_to_iframe()
        self.input(self.expiration_date_field_locator, expiration_date)
        self.driver.switch_to.default_content()

        #cvc input
        self.switch_to_iframe()
        self.input(self.cvc_field_locator, cvc)
        self.driver.switch_to.default_content()

        #zipcode input
        self.switch_to_iframe()
        self.input(self.zip_code_field_locator, zip_code)
        self.driver.switch_to.default_content()

        #submition form
        #clicking to add new payment method
    def click_on_add_payment_method(self):
        self.wait_until_element_is_visible(self.add_payment_method_link_locator, timeout=10).click()

    def is_card_added(self):
        return self.confirm_element_is_displayed(self.success_message_locator)


