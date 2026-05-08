import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class AdornoTest(unittest.TestCase):
    
    def setUp(self):
        # Get the app URL from environment variable
        self.base_url = os.environ.get('APP_URL', 'http://localhost:8081')
        
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
    
    def test_01_homepage_title(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn("Adorno", self.driver.title)
    
    def test_02_navbar_exists(self):
        self.driver.get(self.base_url)
        navbar = self.driver.find_element(By.TAG_NAME, "nav")
        self.assertTrue(navbar.is_displayed())
    
    # ... rest of your 13 test cases (copy from before)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()