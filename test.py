from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

card_info = {
    "card_number": "4242424242424242",
    "exp_month": "12",
    "exp_year": "24",
    "cvc": "123",
    "card_holder": "NGUYEN VAN DUNG",
    "address1": "Ha Noi, Viet Nam",
    "address2": "Ha Noi, Viet Nam",
    "city": "Ha Noi",
    "post_code": "10000",
}

def run():
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r"user-data-dir=C:\Users\khai.dv\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument("profile-directory=Profile 6")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://wallet.google.com/wallet/paymentmethods?utm_campaign=wallet_about&utm_source=website&utm_medium=marketing&pli=1")
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/main/c-wiz/div/div[2]/div[1]/div/section/div[1]/div/div[1]/div/div/div/div/button',
    ).click()
    time.sleep(3)
    # .jfk-button.jfk-button-action.b3-button.b3id-button
    driver.find_element(
        By.CLASS_NAME,
        "jfk-button jfk-button-action b3-button b3id-button",
    ).click()
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[1]',
    ).click()
    time.sleep(2)
    # country - need to check
    driver.find_element(
        By.XPATH,
        '//*[@id=":7b"]',
    ).click()
    # address 1
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[2]/div/div[7]/div/div/div[1]/input',
    ).send_keys(card_info["address1"])
    # address 2
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[2]/div/div[9]/div/div/div[1]/input',
    ).send_keys(card_info["address2"])
    # city
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[2]/div/div[11]/div/div/div[1]/input',
    ).send_keys(card_info["city"])
    # province - need to check
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[2]/div/div[1]/div[24]',
    ).click()
    # postcode
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[2]/div/div[14]/div/div/div[1]/input',
    ).send_keys(card_info["post_code"])
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[1]/div[1]/div/div/div[1]/input',
    ).send_keys(card_info["card_number"])
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input',
    ).send_keys(card_info["exp_month"])
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[1]/div[2]/div[1]/div[2]/div/div[1]/input',
    ).send_keys(card_info["exp_year"])
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[1]/div[2]/div[2]/div/div/div[1]/input',
    ).send_keys(card_info["cvc"])
    driver.find_element(
        By.XPATH,
        '//*[@id="creditCardForm-1"]/div[2]/div/div[1]/input',
    ).send_keys(card_info["card_holder"])

    # driver.find_element(By.NAME, "identifier").send_keys("1hotheart1coldhead@gmail.com")
    # time.sleep(1)
    # try:
    #     driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    #     time.sleep(10000)

    # except:
    #     driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b").click()
    #     time.sleep(10000)


run()