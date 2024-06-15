import time
import pytest
from POM.Loginpage import Loginpage
from POM.Addcustomer import AddCustomer
from POM.SearchCustomer import Searchcustomer
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("***** SearchCustomerByEmail_004 ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***** Login succesful ****")

        self.logger.info("*** Starting Search Customer By Email ****")

        self.addcust = AddCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickOnCustomersMenu()
        time.sleep(5)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)

        self.logger.info("***** searching customer by emailID ****")
        searchcust=Searchcustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        searchcust.Clicksearch()
        time.sleep(2)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("*****  TC_SearchCustomerByEmail_004 Finished  ***** ")