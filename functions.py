import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# Logging format starts here
"""This will format the message style and color"""
FMT = "{message}"  # i.e [INFO] root: Info Message
Formats = {
    logging.DEBUG: f"\33[37m{FMT}\33[0m",  # debug is gray
    logging.INFO: f"\33[36m{FMT}\33[0m",  # Info is green
    logging.WARNING: f"\33[33m{FMT}\33[0m",  # Warning is yellowish
    logging.ERROR: f"\33[31m{FMT}\33[0m",  # Error is red
    logging.CRITICAL: f"\33[1m\33[33m{FMT}\33[0m",  # Critical is yellowish

}


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_fmt = Formats[record.levelno]
        formatter = logging.Formatter(log_fmt, style="{")
        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logging.basicConfig(
    level=logging.INFO,  # it will only start printing from Info and downwards (Info, Warning, Error and Critical)
    handlers=[handler],
    # filename=r"C:\Users\User\PycharmProjects\Selenium\Data\logfile.log"
)

# Logging format ends here

browser = webdriver.Chrome(ChromeDriverManager().install())


def ElementIsNotPresent(Element, ElemLocator):
    """
    This function checks if elements are not visible
    :param Element: ID, Xpath or Name
    :param ElemLocator: By.ID, By.XPATH, By.NAME
    :return: Element is Visible message, Element is Invisble message or Exception message
    """
    try:
        browser.implicitly_wait(3)
        Elem = browser.find_element(ElemLocator, Element)
        if Elem.is_displayed():
            # print("Element," + Element + " is visible, while expected to be invisible - FAILED.")
            logging.error("Element, {} is visible, while expected to be invisible - FAILED.".format(Element))
        else:
            logging.info("Element, {} is Invisible - PASSED.".format(Element))

    except Exception as e:
        # print(e)
        logging.info("Element, {} is Invisible - PASSED.".format(Element))


def openUrl(URL):
    try:
        browser.get(URL)
        browser.maximize_window()
        logging.info("\nBrowser opened successful: {}\n".format(URL))
    except Exception as e:
        logging.critical(e)
        logging.error("\nBrowser open unsuccessful: {}\n".format(URL))


def clickOnElement(elementID, elemenLctType, value):
    if value.lower() == "invisible":
        ElementIsNotPresent(elementID, elemenLctType)
    else:
        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
            element.click()
            logging.info(f'clickOnElement: {elementID} by element locator type {elemenLctType} -- PASSED')

        except Exception as e:
            logging.critical(e)
            logging.error(f'clickOnElement: {elementID} by element locator type {elemenLctType} -- FAILED')


def selectFromDrpDwn(elementID, elemenLctType, value):
    try:
        select = Select(WebDriverWait(browser, 15).until(EC.element_to_be_clickable((elemenLctType, elementID))))
        select.select_by_visible_text(value)
        logging.info(f"selectFromDrpDwn: {elementID} by element locator type {elemenLctType} - PASSED.")
    except Exception as e:
        logging.critical(e)
        logging.error(f"selectFromDrpDwn: {elementID} by element locator type {elemenLctType}- FAILED.")


def typeInElement(elementID, elemenLctType, value):
    if value.startswith("Val_"):  # only deals data that start with "Val_"
        # This filters out Val_ from the whole Data value
        TheSuffix = value.removeprefix("Val_")  # == Val_xxxx.remove(Val_) == xxxx
        ThePrefix = value.removesuffix(TheSuffix)  # == Val_xxxx.remove(xxxx) == Val_

        if ThePrefix == "Val_":
            validateFldValue(elementID, elemenLctType, TheSuffix)
    else:
        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
            element.clear()
            element.send_keys(value)
            logging.info(f'typeInElement: {elementID} by element locator type {elemenLctType} -- PASSED')
        except Exception as e:
            logging.critical(e)
            logging.error(f'typeInElement: {elementID} by element locator type {elemenLctType} -- FAILED')


def validateValue(elementID, elemenLctType, assertValue):
    if assertValue.lower() == "invisible":
        ElementIsNotPresent(elementID, elemenLctType)
    else:
        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
            value = element.text
            if value == assertValue:
                logging.info(f"Expected value: {assertValue}; Value Found: {value}.")
                logging.info(f"Assert value: {assertValue} found -- PASSED")
            else:
                logging.error(f"Expected value: {assertValue}; Value Found: {value}.")
                logging.error(f"Assert value: {assertValue} not found -- FAILED")

        except Exception as e:
            logging.critical(e)
            logging.error(f'validateValue: {elementID} by element locator type {elemenLctType} -- FAILED')


def validateFldValue(elementID, elemenLctType, assertValue):
    if assertValue.lower() == "invisible":
        ElementIsNotPresent(elementID, elemenLctType)
    else:
        try:
            Elem = browser.find_element(by=elemenLctType, value=elementID)
            value = Elem.get_attribute("value")
            if value == assertValue:
                logging.info(f"Expected value: {assertValue}; Value Found: {value}.")
                logging.info(f"Assert value: {assertValue} found -- PASSED")
            else:
                logging.error(f"Expected value: {assertValue}; Value Found: {value}.")
                logging.error(f"Assert value: {assertValue} not found -- FAILED")

        except Exception as e:
            logging.critical(e)
            logging.error(f'validateValue: {elementID} by element locator type {elemenLctType} -- FAILED')


# Read file function
def readfile(Filepath):
    df = pd.read_csv(Filepath, sep=",", dtype=str)  # , sep='delimiter'
    return df


ROOT_DIR = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '..'))
