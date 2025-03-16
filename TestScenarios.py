import json
import os
import pathlib
import time

import pytest
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class TestLinkChrome:
    def load_params_from_json(json_path):
        with open(json_path) as f:
            return json.load(f)

    @pytest.mark.parametrize("driver", load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"), indirect=True)
    def test_scenarios(self, driver):
        driver.get("https://www.lambdatest.com/selenium-playground")

        simple_form_demo_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
        simple_form_demo_link.click()

        assert "simple-form-demo" in driver.current_url
        print("Test Passed: URL contains 'simple-form-demo'")

        message = "Welcome to LambdaTest"

        message_textbox = driver.find_element(By.ID, "user-message")
        message_textbox.send_keys(message)

        # Step 6: Click the "Click Get Checked Value" button
        get_value_button = driver.find_element(By.ID, "showInput")
        get_value_button.click()

        your_message = driver.find_element(By.ID, "message").text
        assert your_message == message
        print(f"Test Passed: 'Your Message:' displays the correct message: {your_message}")

    @pytest.mark.parametrize("driver",
                             load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"),
                             indirect=True)
    def test_scenario_2(self, driver):
        driver.get("https://www.lambdatest.com/selenium-playground")

        drag_and_drop_sliders_link = driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders")
        drag_and_drop_sliders_link.click()

        slider = driver.find_element(By.XPATH, "//input[@type='range' and @value='15']")  # Slider with default value 15
        value_display = driver.find_element(By.XPATH, "//output[@id='rangeSuccess']")  # Value display span

        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(214,
                                                     0).release().perform()  # Adjust the offset value to drag the slider towards 95

        assert value_display.text == "95"
        print("Test Passed: The slider value is correctly set to 95")

    @pytest.mark.parametrize("driver",
                             load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"),
                             indirect=True)
    def test_scenario_3(self, driver):
        driver.get("https://www.lambdatest.com/selenium-playground")

        input_form_submit_link = driver.find_element(By.LINK_TEXT, "Input Form Submit")
        input_form_submit_link.click()

        submit_button = driver.find_element(By.CLASS_NAME, "bg-lambda-900")
        submit_button.click()

        error_message = driver.find_element(By.CSS_SELECTOR, "input:invalid")
        assert "Please fill out this field" in error_message.get_attribute("validationMessage")
        print("Test Passed: 'Please fill out this field' error message is displayed.")

        name_field = driver.find_element(By.NAME, "name")
        name_field.send_keys("Ramya")

        email_field = driver.find_element(By.ID, "inputEmail4")
        email_field.send_keys("ramya@gmail.com")

        password_field = driver.find_element(By.ID, "inputPassword4")
        password_field.send_keys("Ramyasree@123")

        company_field = driver.find_element(By.ID, "company")
        company_field.send_keys("persistent")

        websitename_field = driver.find_element(By.ID, "websitename")
        websitename_field.send_keys("www.persistentsystems.com")

        country_dropdown = driver.find_element(By.NAME, "country")
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text("United States")

        city_field = driver.find_element(By.ID, "inputCity")
        city_field.send_keys("California")

        address1_field = driver.find_element(By.ID, "inputAddress1")
        address1_field.send_keys("Street 1, House 123")

        address2_field = driver.find_element(By.ID, "inputAddress2")
        address2_field.send_keys("GL Street")

        state_field = driver.find_element(By.ID, "inputState")
        state_field.send_keys("Cali")

        zip_field = driver.find_element(By.ID, "inputZip")
        zip_field.send_keys("123456")
        submit_button.click()

        success_message = driver.find_element(By.CLASS_NAME, "success-msg")
        assert "Thanks for contacting us, we will get back to you shortly." in success_message.text
        print("Test Passed: Success message is displayed.")
