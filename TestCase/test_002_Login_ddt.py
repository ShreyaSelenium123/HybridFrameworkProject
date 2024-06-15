import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from POM.Loginpage import Loginpage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import Utilityxl
import time
from selenium.webdriver.common.by import By


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\TestDataLogin.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        self.logger.info("***Login_Test002_DDT*****")
        self.logger.info("****Verifying Login test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.rows = Utilityxl.getRowcount(self.path, "Sheet1")
        print("Number of Rows in a excel sheet:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = Utilityxl.readData(self.path, 'Sheet1', r, 1)
            self.password = Utilityxl.readData(self.path, 'Sheet1', r, 2)
            self.exp = Utilityxl.readData(self.path, 'Sheet1', r, 3)

            self.logger.info(f"Attempting login with username: {self.user} and password: {self.password}")

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)

            try:
                # Explicit wait before clicking login
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
                )
                self.lp.clicklogin()

                # Wait for the page title to change
                WebDriverWait(self.driver, 20).until(
                    EC.title_contains("Dashboard")
                )
            except TimeoutException:
                self.logger.error("Timeout occurred while waiting for login button or title change")
                lst_status.append("Fail")
                self.driver.save_screenshot("timeout_exception.png")
                continue

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")

            try:
                # Ensure logout before next iteration
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
                )
                self.lp.clickLogout()
            except TimeoutException:
                self.logger.error("Timeout occurred while waiting for logout link")
                self.driver.save_screenshot("logout_timeout_exception.png")
                continue

        if "Fail" not in lst_status:
            self.logger.info("**DDT Login test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("**DDT Login test Failed ***")
            self.driver.close()

