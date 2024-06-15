import pytest
from selenium import webdriver
from POM.Loginpage import Loginpage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):

        self.logger.info("****Test_001_Login***")
        self.logger.info("****Verifying home Page ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****Test passed***")
        else:
            self.driver.save_screenshot(r".\\Screenshot\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.info("****Test_Failed ***")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Verifying Login test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****Login passed*****")
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****Login Failed***")
            assert False
