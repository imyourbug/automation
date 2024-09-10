from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

card_info = {
    "card_number": "4089051002999430",
    "exp_month": "07",
    "exp_year": "29",
    "cvc": "704",
    "card_holder": "NGUYEN VAN DUNG",
    "address1": "Ha Noi, Viet Nam",
    "address2": "Ha Noi, Viet Nam",
    "city": "Ha Noi",
    "post_code": "10000",
}

desired_caps = {
    "platformName": "Android",
    "deviceName": "Redmi Note 7",
    "platformVersion": "10",
    "udid": "91c2c4d7",
    "newCommandTimeout": 300,  # Timeout for waiting for new commands
    "connectTimeout": 20
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(1)

import unicodedata
import re


def convert_to_slug(text):
    # Normalize Unicode characters to remove accents (decompose characters)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")

    # Convert to lowercase
    text = text.lower()

    # Replace spaces with hyphens
    text = text.replace(" ", "-")

    # Remove any non-alphanumeric characters except for hyphens
    text = re.sub(r"[^a-z0-9-]", "", text)

    return text

def unlock_screen():
    driver.press_keycode(224)
    # Create a TouchAction object
    # touch_action = TouchAction(driver)
    # # Perform a swipe action
    # touch_action.press(x=100, y=100)  # Starting point (x, y)
    # touch_action.wait(ms=500)  # Wait for 500 ms
    # touch_action.move_to(x=100, y=-500)  # Ending point (x, y)
    # touch_action.release()  # Release the touch action
    # touch_action.perform()  # Perform the action

try:
    # Unlock the screen
    unlock_screen()

    # click wallet
    driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Wallet"]').click()
    # Click add to wallet
    driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Thêm vào Wallet"]').click()
    # Click add payment card
    driver.find_element(MobileBy.XPATH, '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.gms.optional_pay:id/AddItemContent"]/android.view.ViewGroup[1]').click()
    # Click add payment method
    driver.find_element(MobileBy.XPATH, '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.gms.optional_pay:id/AddPaymentMethodFragmentRecyclerViewRight"]/android.widget.LinearLayout[1]/android.view.ViewGroup').click()

    edit_texts = driver.find_elements_by_class_name("android.widget.EditText")
    index = 0
    for edit_text in edit_texts:
        if index == 0:
            edit_text.send_keys(card_info["card_number"])
        elif index == 1:
            edit_text.send_keys("{}/{}".format(card_info["exp_month"], card_info["exp_year"]))
        elif index == 2:
            edit_text.send_keys(card_info["cvc"])
        else:
            break
        index += 1

    driver.find_element(
        MobileBy.XPATH, '//android.widget.Button[@content-desc="edit button"]'
    ).click()
    time.sleep(2)
    #
    for btn in driver.find_elements_by_class_name("android.widget.Button"):
        if convert_to_slug(btn.get_attribute("text")) == "tuy-chon-khac":
            btn.click()
            break
    #
    for btn in driver.find_elements_by_class_name("android.widget.Button"):
        if convert_to_slug(btn.get_attribute("text")) == "luu-va-tiep-tuc":
            btn.click()
            break
    print("Done")

finally:
    # Quit the driver
    driver.quit()
