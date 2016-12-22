from selenium.webdriver.common.by import By


class BuyNowLocs(object):

    QAFURL = "https://qaorigin.metrofax.com/buy-now/fax-numbers"
    S1_COUNTRY_US = (By.XPATH, '//select[@id="numberchooser-country"] \
                               /option[text()="United States"]')
    S1_COUNTRY_CANADA = (By.XPATH, '//select[@id="numberchooser-country"] \
                                   /option[text()="Canada"]')
    S1_STATE_DDL = (By.ID, "NumberChooser-stateddl")
    S1_STATE_CAL = (By.XPATH,
                    '//select[@id="NumberChooser-stateddl"] \
                    /option[text()="California"]')
    S1_AREA_CODE_DDL = (By.ID, "NumberChooser-cityddl")
    S1_AREA_CODE_800 = (By.XPATH, '//select[@id="NumberChooser-cityddl"] \
                                  /option[text()="800 - Toll Free"]')

    # Section 1 Plan Selection ------------------------------------------------

    # Essential ---------------------------------------------------------------
    S1_ESSENTIAL_MONTH_RDIO = (By.ID, "essential-month")
    S1_ESSENTIAL_ANNUAL_RDIO = (By.ID, "essential-year")
    S1_ESSENTIAL_NEXT_BTN = (By.CLASS_NAME, "btnessential")
    # Value -------------------------------------------------------------------
    S1_VALUE_MONTH_RDIO = (By.ID, "value-month")
    S1_VALUE_ANNAUL_RDIO = (By.ID, "value-year")
    S1_VALUE_NEXT_BTN = (By.CLASS_NAME, "btnvalue")
    # Professional ------------------------------------------------------------
    S1_PRO_MONTH_RDIO = (By.ID, "professional-month")
    S1_PRO_MONTH_ANNUAL_RDIO = (By.ID, "professional-year")
    S1_PRO_NEXT_BTN = (By.CLASS_NAME, "btnprofessional")

    # Section 2 Account Setup -------------------------------------------------
    S2_CONTACT_EMAIL_INPT = (By.ID, "EmailAddress1")
    S2_NEXT_BTN = (By.ID, "sf_dyno-2")

    # Section 3 Billing Info --------------------------------------------------
    S3_FNAME_INPT = (By.CLASS_NAME, "firstname")
    S3_LNAME_INPT = (By.CLASS_NAME, "lastname")
    S3_COMPANY_NAME_INPT = (By.CLASS_NAME, "companyName")
    S3_ADDRESS_1_INPT = (By.CLASS_NAME, "address1")
    S3_ADDRESS_2_INPT = (By.CLASS_NAME, "address2")
    S3_COUNTRY_DDL = (By.CLASS_NAME, "country")
    S3_CITY_INPT = (BY.CLASS_NAME, "city")
    S3_STATE_DDL = (By.CLASS_NAME, "state")
    S3_ZIPCODE_INPT = (By.CLASS_NAME, "zipcode")
    S3_PHONE_INPT = (By.CSS_SELECTOR, "phone")
    # Credit Card Locators ----------------------------------------------------
    S3_CARD_HOLDER_NAME_INPT = (By.CLASS_NAME, "creditcardname")
    S3_CARD_TYPE_DDL = (By.CLASS_NAME, "creditcardtype")
    S3_CC_NUM_INPT = (By.CLASS_NAME, "creditcardnumber")
    S3_MONTH_EXP_DDL = (By.CLASS_NAME, "creditcard-exp-month")
    S3_YEAR_EXP_DDL = (By.CLASS_NAME, "creditcard-exp-year")
    S3_CVV_INPT = (By.CLASS_NAME, "cvv")
    S3_AGREEMENT_INPT = (By.CLASS_NAME, "customer-agreement")
    # Order Confirmation
    S4_MONTHY_FEE_LBL = (By.ID, "paidsignup_periodicFee")
    S4_ACTIVATION_FEE_LBL = (By.ID, "paidsignup_activationFee")
    S4_PAGES_INCLUDED_LBL = (By.ID, "paidsignup_FreePages")
    S4_YOUR_NUM_LBL = (By.XPATH,
                       '//*[@id="Contentplaceholder1_C003_Col01"]/ \
                        div[1]/div[2]/p[1]/strong')
    S4_YOUR_PIN_LBL = (By.XPATH,
                       '//*[@id="Contentplaceholder1_C003_Col01"]/ \
                        div[1]/div[2]/p[2]/strong')
    S4_LOGIN_BTN = (By.XPATH,
                    '//*[@id="Contentplaceholder1_C003_Col01"] \
                     /div[1]/div[2]/p[3]/a)'
