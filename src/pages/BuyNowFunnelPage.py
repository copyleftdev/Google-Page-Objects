from elements.FunnelElement import BasePageElement
from locators.Funnels.BuyNow.FunnelLocs import BuyNowLocs
from src.Utils.faker import Factory

fake = Factory.create()

class BuyNowFunnelPage(object):

    def __init__(self, driver):
        self.driver = driver

    def populate_stage_1_us_essential_monthly(self):
        """root vector https://qaorigin.metrofax.com/buy-now/fax-numbers"""
        country = self.driver.find_element(*BuyNowLocs.S1_COUNTRY_US)
        state = self.driver.find_element(*BuyNowLocs.S1_COUNTRY_CANADA)
        areacode = self.driver.find_element(*BuyNowLocs.S1_AREA_CODE_800)
        essential_monthy = self.driver.find_element(
                                       *BuyNowLocs.S1_ESSENTIAL_MONTH_RDIO)
        stage_two = self.driver.find_element(*BuyNowLocs.S1_ESSENTIAL_NEXT_BTN)
        country.click()
        state.click()
        areacode.click()
        essential_monthy.click()
        #stage_two.click()
