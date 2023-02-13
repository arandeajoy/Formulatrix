import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestOrder(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_order(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[10]/h2").text

        self.assertEqual(response_message, 'Thank you for your purchase!')

    def test_a_failed_order_with_empty_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_country_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Country and City')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_city_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Country and City')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_credit_cart_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Name and Creditcard.')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_month_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Month and Year.')

        Alert(browser).accept()

    def test_a_failed_order_with_empty_year_order_form(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Month and Year.')

        Alert(browser).accept()

    def test_a_failed_order_with_name_contain_numbers(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy312")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Name Cannot Contain Numbers')

    def test_a_failed_order_with_name_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy*#")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Name Cannot Contain Symbols')

    def test_a_failed_order_with_country_contain_numbers(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia45")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Country Cannot Contain Numbers')

    def test_a_failed_order_with_country_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia*#")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Country Cannot Contain Symbols')

    def test_a_failed_order_with_city_contain_numbers(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati03")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'City Cannot Contain Numbers')

    def test_a_failed_order_with_city_contain_simbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati*#")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'City Cannot Contain Symbols')

    def test_a_failed_order_with_credit_card_contain_letters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555qwerty")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Credit Card Cannot Contain Letters')

    def test_a_failed_order_with_credit_card_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555*#")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Credit Card Cannot Contain Symbols')

    def test_a_failed_order_with_month_contain_letters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("february")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Month Cannot Contain Letters')

    def test_a_failed_order_with_month_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02*#")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Month Cannot Contain Symbols')

    def test_a_failed_order_with_Year_contain_letters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024qwerty")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Year Cannot Contain Letters')

    def test_a_failed_order_with_Year_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[2]/div/a").click()
        time.sleep(2)
        Alert(browser).accept()
        time.sleep(2)
        browser.find_element(By.ID,"cartur").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        browser.find_element(By.ID,"name").send_keys("joy")
        time.sleep(1)
        browser.find_element(By.ID,"country").send_keys("indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"city").send_keys("pati")
        time.sleep(1)
        browser.find_element(By.ID,"card").send_keys("55555")
        time.sleep(1)
        browser.find_element(By.ID,"month").send_keys("02")
        time.sleep(1)
        browser.find_element(By.ID,"year").send_keys("2024*#")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Year Cannot Contain Symbols')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()