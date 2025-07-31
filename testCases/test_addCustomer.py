import random
import string
import time

import pytest

from pageObjects.LoginPage import Login
from pageObjects.add_customer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("*********TEst_003_AddCustomer")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login Successful*******")

        self.logger.info("*******Starting Add Customer Test**********")
        self.cust=AddCustomer(self.driver)
        time.sleep(10)
        self.cust.clickOnCustomer()
        time.sleep(5)

        self.cust.clickONCustomers_1()

        self.cust.clickONNewButton()
        self.logger.info("******Provide customer details*******")
        self.email=random_generator()+"@gmail.com"
        self.cust.enterEmail(self.email)
        self.cust.enterPassword('test123')
        self.cust.enterFirstName("Bhanu")
        self.cust.enterLastName("Prakash")
        self.cust.clickOnGender()
        self.cust.enterCompanyName("Aptean")
        self.cust.istaxexempt_Selected()
        #self.cust.selectNewsLetter()
        self.cust.clickOnCustomerRoles("Guests")
        self.cust.selectVendor("Vendor 2")
        self.cust.clickOnSave()

        time.sleep(10)
        self.driver.close()