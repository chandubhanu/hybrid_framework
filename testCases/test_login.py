import os

import pytest
import self
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup


class Test_001_login:

   baseURL="https://admin-demo.nopcommerce.com/"
   username="admin@yourstore.com"
   password="admin"

   def test_homePageTItle(self,setup):
     self.driver = setup
     self.driver.get(self.baseURL)
     actual_title=self.driver.title
     if actual_title=="nopCommerce demo store. Login":
         assert True
     else:
         self.driver.save_screenshot("\\Screenshots\\"+"test_homePageTitle.png")
         assert False
     self.driver.close()


   def test_login(self,setup):
       self.driver = setup
       self.driver.get(self.baseURL)
       self.lp=Login(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setPassword(self.password)
       self.lp.clickLogin()
       act_title=self.driver.title

       screenshot_path = os.path.join(os.getcwd(), "Screenshots", "test_login.png")

       if act_title == "Dashboard / nopCommerce administration":
           assert True
       else:
           self.driver.save_screenshot(screenshot_path)
           assert False

       self.driver.close()

