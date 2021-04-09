""" This file contains  Selenium tests """
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class TestAppAccount(StaticLiveServerTestCase):
    """Test correct register form submission"""

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_form_submission_with_button(self):
        self.driver.get(str(self.live_server_url) + '/compte/inscription/')
        username_input = self.driver.find_element_by_id('id_username')
        email_input = self.driver.find_element_by_id('id_email')
        password1_input = self.driver.find_element_by_id('id_password1')
        password2_input = self.driver.find_element_by_id('id_password2')
        submission_button = self.driver.find_element_by_class_name(
            'btn-primary')

        username_input.send_keys('test')
        email_input.send_keys('test@gmail.com')
        password1_input.send_keys('123selenium')
        password2_input.send_keys('123selenium')
        submission_button.click()
        time.sleep(5)
        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + '/', redirection_url)