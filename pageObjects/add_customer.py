import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer():
    # Add customer Page:
    customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customers_1_xpath = "(//p[contains(text(),'Customers')])[2]"
    new_button_xpath = "//i[@class='fas fa-square-plus']"
    email_xpath = "//input[@id='Email']"
    password_xpath = "//input[@id='Password']"
    firstname_xpath = "//input[@id='FirstName']"
    lastname_xpath = "//input[@id='LastName']"
    gender_xpath = "//input[@id='Gender_Male']"
    company_name_xpath = "//input[@id='Company']"
    istaxexempt_xpath = "//input[@id='IsTaxExempt']"
    newsletter_xpath = "(//input[@role='searchbox'])[1]"
    nopadminstore_xpath = "//li[contains(text(),'nopCommerce admin demo store')]"
    customerroles_xpath = "//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']"
    registered_xpath = "(//li[@id='select2-SelectedCustomerRoleIds-result-e0qr-3'])[1]"
    admin_xpath = "(//li[@id='select2-SelectedCustomerRoleIds-result-kkr7-1'])[1]"
    guests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-gx3p-4']"
    vendor_xpath = "//select[@id='VendorId']"
    vendors_xpath = "(//li[@id='select2-SelectedCustomerRoleIds-result-s4k8-5'])[1]"
    save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomer(self):
        self.driver.find_element(By.XPATH, self.customers_xpath).click()

    def clickONCustomers_1(self):
        self.driver.find_element(By.XPATH, self.customers_1_xpath).click()

    def clickONNewButton(self):
        self.driver.find_element(By.XPATH, self.new_button_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enterFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(firstname)

    def enterLastName(self, lastname):  # Renamed to fix the duplicate
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lastname)

    def clickOnGender(self):
        self.driver.find_element(By.XPATH, self.gender_xpath).click()

    def enterCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.company_name_xpath).send_keys(companyname)

    def istaxexempt_Selected(self):
        checkbox = self.driver.find_element(By.XPATH, self.istaxexempt_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def selectNewsLetter(self):
        try:
            newsletter_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.newsletter_xpath))
            )
            newsletter_input.click()
            time.sleep(1)

            store_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.nopadminstore_xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", store_option)
            self.driver.execute_script("arguments[0].click();", store_option)

            print("✅ Newsletter option selected.")
        except Exception as e:
            print("❌ Failed to select newsletter option:", str(e))
            self.driver.save_screenshot("newsletter_error.png")
            raise

    def clickOnCustomerRoles(self, role):
        def clickOnCustomerRoles(self, role):
            self.driver.find_element(By.XPATH, self.customerroles_xpath).click()
            time.sleep(5)
            if role == 'Registered':
                self.listitem = self.driver.find_element(By.XPATH, self.registered_xpath)
            elif role == "Adminstrators":
                self.listitem = self.driver.find_element(By.XPATH, self.admin_xpath)
            elif role == "Guests":
                self.driver.find_element(By.XPATH, self.registered_xpath).click()
                self.listitem = self.driver.find_element(By.XPATH, self.guests_xpath)
            elif role == "Vendors":
                self.listitem = self.driver.find_element(By.XPATH, self.vendors_xpath)
            else:
                self.listitem = self.driver.find_element(By.XPATH, self.guests_xpath)

            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", self.listitem)





    def selectVendor(self, value):
        drp_down = self.driver.find_element(By.XPATH, self.vendor_xpath)
        dropdown = Select(drp_down)
        dropdown.select_by_visible_text(value)

    def clickOnSave(self):  # Fixed typo and added 'self'
        self.driver.find_element(By.XPATH, self.save_xpath).click()
