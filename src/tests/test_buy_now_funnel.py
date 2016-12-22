import unittest
from selenium import webdriver
from srcpages.BuyNowFunnelPage import BuyNowFunnelPage


class BuyNowSignupFunnelTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_stage1_us__essential_monthly(self):
        self.driver.get("https://qaorigin.metrofax.com/buy-now/fax-numbers")
        stage1_landing = BuyNowSignupFunnelTest(self.driver)
        stage1_landing.populate_stage_1_us_essential_monthly()

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
