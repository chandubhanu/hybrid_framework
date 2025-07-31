from selenium.webdriver.common.by import By

class SearchCustomer:
    def __init__(self, driver):
        self.driver = driver

    txtEmail_id = "SearchEmail"
    txtFirstname_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchresults_Xpath = "//div[@id='customers-grid_processing']"  # Fixed typo in id
    table_xpath = "//table[@id='customers-grid']"
    tblRow_Xpath = "//table[@id='customers-grid']//tbody/tr"
    tblColumn_Xpath = "//table[@id='customers-grid']//tbody/tr[1]/td"

    def email(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)  # fixed typo

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstname_id).clear()
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstname)  # fixed typo

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)  # fixed typo

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblRow_Xpath))  # fixed find_element → find_elements

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tblColumn_Xpath))  # fixed find_element → find_elements

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):  # added parentheses to call function
            emailid = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[2]"
            ).text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            fullname = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[3]"
            ).text
            if fullname == name:
                flag = True
                break
        return flag
