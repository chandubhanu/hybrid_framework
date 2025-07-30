import os
import time

from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excel_utils


class Test_002_DDT_login:

   baseURL=ReadConfig.getApllicationURL()
   path=".//testData//LoginData.xlsx"
   logger=LogGen.loggen()

   def test_DDT_login(self,setup):
       self.logger.info("*****Verifying the login test********")
       self.logger.info("*****Verifying the login test********")
       self.driver = setup
       self.driver.get(self.baseURL)
       self.lp=Login(self.driver)

       self.rows_count=excel_utils.getRowCount(self.path,'Sheet1')
       list_status=[]  #empty list
       for r in range(2,self.rows_count+1):
            self.user= excel_utils.readData(self.path,'Sheet1',r,1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp = excel_utils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"


            if act_title == exp_title:
                if self.exp=="Pass":
                 self.logger.info("*****passed********")
                 self.lp.clickLogout()
                 list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*****Failed********")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=="Pass":
                 self.logger.info("*****Failed********")
                 list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*****passed********")
                    list_status.append("pass")

       if "Fail" not in list_status:
           self.logger.info("****Login DDT test passed*****")
           self.driver.close()
           assert True
       else:
          self.logger.info("****Login DDT test Failed*****")
          self.driver.close()
          assert False

