import requests
import dataEntryAutomator
from selenium.webdriver.chrome.service import Service


CHROME_WEBDRIVER_PATH = "Enter the path to your chrome webdriver here"
FORM_URL = "Enter the link to the form you created here"
SOUP_URL = "Enter the Zillow link including all filters here"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.48"
                  "96.60 Safari/537.36"
}

response = requests.get(SOUP_URL, headers=HEADERS)
contents = response.text

ser = Service(CHROME_WEBDRIVER_PATH)

automator = dataEntryAutomator.DataEntryAutomator(contents, ser)
automator.get_info()
automator.fill_form(FORM_URL)
