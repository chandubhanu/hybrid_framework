import os

from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:

   baseURL=ReadConfig.getApllicationURL()
   username=ReadConfig.getuserName()
   password=ReadConfig.getPassword()
   logger=LogGen.loggen()

   def test_homePageTItle(self,setup):
     self.logger.info("*****Test_001_login********")
     self.logger.info("*****Verifying Home Page Title********")
     self.driver = setup
     self.driver.get(self.baseURL)
     actual_title=self.driver.title
     if actual_title=="nopCommerce demo store. Login":
         assert True
         self.driver.close()
         self.logger.info("*****Home Page title is passed********")
     else:
         self.driver.save_screenshot("\\Screenshots\\"+"test_homePageTitle.png")
         self.driver.close()
         self.logger.info("*****Home Page title is failed********")
         assert False


   def test_login(self,setup):
       self.logger.info("*****Verifying the login test********")
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
           self.driver.close()
           self.logger.info("*****Login test title is passed********")
       else:
           self.driver.save_screenshot(screenshot_path)
           self.logger.error("*****Login test title is failed********")
           assert False
           self.driver.close()
