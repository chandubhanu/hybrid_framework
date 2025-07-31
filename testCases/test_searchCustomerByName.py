import time
from re import search

import pytest
import self

from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.add_customer import AddCustomer
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_SearchCustomer():
 baseURL = ReadConfig.getApplicationURL()
 username = ReadConfig.getuserName()
 password = ReadConfig.getPassword()
 logger = LogGen.loggen()


 @pytest.mark.regression
 def test_searchCustomerByName(self,setup):
  self.driver=setup
  self.driver.get(self.baseURL)
  self.driver.maximize_window()
  self.lp=Login(self.driver)
  self.lp.setUserName(self.username)
  self.lp.setPassword(self.password)
  self.lp.clickLogin()

  self.cus=AddCustomer(self.driver)
  self.cus.clickOnCustomer()
  time.sleep(10)
  self.cus.clickONCustomers_1()

  search = SearchCustomer(self.driver)
  search.setFirstName("Steve")
  search.clickSearchButton()
  time.sleep(10)
  status=search.searchCustomerByName("Steve Gates")
  assert True==status



