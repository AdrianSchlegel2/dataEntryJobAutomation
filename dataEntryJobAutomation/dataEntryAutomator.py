from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class DataEntryAutomator:
    def __init__(self, contents, ser):
        self.soup = BeautifulSoup(contents, "html.parser")
        self.links = []
        self.prices = []
        self.addresses = []
        self.driver = webdriver.Chrome(service=ser)

    def get_info(self):
        scraped_prices = self.soup.find_all("div", class_="list-card-price")
        self.prices = [price.text[:6] for price in scraped_prices if price in scraped_prices]
        scraped_links = self.soup.find_all("a", class_="list-card-link list-card-link-top-margin")
        self.links = [link.get("href") for link in scraped_links if link in scraped_links]
        scraped_addresses = self.soup.find_all("address", class_="list-card-addr")
        self.addresses = [address.text for address in scraped_addresses if address in scraped_addresses]

    def fill_form(self, form):
        self.driver.get(form)
        self.driver.maximize_window()
        print(f"{len(self.prices)}\n{len(self.links)}\n{len(self.addresses)}")
        for n in range(len(self.links)):
            try:
                address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div'
                                                                   '[2]/div/div[1]/div/div[1]/input')
                address_input.send_keys(self.addresses[n])
                price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div'
                                                                 '[2]/div/div[1]/div/div[1]/input')
                price_input.send_keys(self.prices[n])
                link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div'
                                                                '[2]/div/div[1]/div/div[1]/input')
                link_input.send_keys(self.links[n])
                self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
                sleep(3)
                self.driver.find_element(By.LINK_TEXT, 'Weitere Antwort senden').click()
                sleep(4)
            except IndexError:
                continue

        sleep(100)

