import unittest
import time
import random
import string
from selenium import webdriver 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        randomword = ''.join(random.choices(string.ascii_lowercase, k=6))
        browser.find_element(By.ID,"sign-username").send_keys(randomword)
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Sign up successful.')

        Alert(browser).accept()

    def test_a_failed_register_with_already_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'This user already exist.')

        Alert(browser).accept()

    def test_a_failed_register_with_empty_username(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_failed_register_with_empty_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_failed_register_with_empty_username_password(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        browser.find_element(By.ID,"sign-username").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Please fill out Username and Password.')

        Alert(browser).accept()

    def test_a_failed_register_with_username_contain_symbols(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        randomword = ''.join(random.choices(string.ascii_lowercase + string.punctuation, k=6))
        browser.find_element(By.ID,"sign-username").send_keys(randomword)
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("formulatrix")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Username cannot contain symbols.')

        Alert(browser).accept()

    def test_a_failed_register_with_password_less_8_Characters(self): 
        browser = self.browser
        browser.get("https://www.demoblaze.com/index.html")
        time.sleep(2)
        browser.find_element(By.ID,"signin2").click()
        time.sleep(1)
        randomword = ''.join(random.choices(string.ascii_lowercase, k=6))
        browser.find_element(By.ID,"sign-username").send_keys(randomword)
        time.sleep(1)
        browser.find_element(By.ID,"sign-password").send_keys("for")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]").click()
        time.sleep(2)

        response_message = Alert(browser).text

        self.assertEqual(response_message, 'Password must contain at least 8 characters')

        Alert(browser).accept()

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()