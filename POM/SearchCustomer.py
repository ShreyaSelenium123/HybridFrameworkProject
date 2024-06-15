from selenium import webdriver
from selenium.webdriver.common.by import By

class Searchcustomer:
    txt_Email_id="SearchEmail"
    txt_FirstName_id ="SearchFirstName"
    txt_LastName_id="SearchLastName"
    btn_Search_id="search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_Email_id).clear()

        self.driver.find_element(By.ID,self.txt_Email_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_FirstName_id).clear()
        self.driver.find_element(By.ID,self.txt_FirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txt_LastName_id).clear()
        self.driver.find_element(By.ID,self.txt_LastName_id).send_keys(lname)

    def Clicksearch(self):
        self.driver.find_element(By.ID,self.btn_Search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH,self.table_xpath)
          emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH,self.table_xpath)
          name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag
