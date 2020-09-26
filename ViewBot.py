from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from VideosBot import VideosBot

import random
import time
import sys

class ViewBot:
    def __init__(self, number_of_drivers):
        self.number_of_drivers = number_of_drivers
        self.drivers = []
        self.currProxy = None
        self.proxies = []
        self.videosBot = VideosBot()
        self.init_proxies()
        self.reset_drivers()

    def get_next_proxy(self):
        if self.currProxy is None:
            self.currProxy = 0
        else:
            self.currProxy = (self.currProxy + 1) % len(self.proxies)

        return self.proxies[self.currProxy]

    def create_chrome_driver(self):
        chrome_options = EdgeOptions()

        proxy = self.get_next_proxy()
        print("CurrProxy: " + proxy)

        chrome_options.add_argument('--proxy-server=%s' % proxy)
        return webdriver.Chrome("C:\\Windows.old\\Users\\Public\\chromedriver.exe", options=chrome_options)

    def create_edge_driver(self):
        options = Options()
        options.use_chromium = True
        proxy = self.get_next_proxy()

        print("CurrProxy: " + proxy)
        options.add_argument('--proxy-server=%s' % proxy)

        return Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", options=options)

    def init_proxies(self):
        proxies_file = open("validProxies", "r")
        self.proxies = proxies_file.read().splitlines()

    def reset_drivers(self):
        self.delete_running_drivers()

        for driverIndex in range(self.number_of_drivers):
            new_driver = self.create_chrome_driver()
            self.drivers.append(new_driver)

    def delete_running_drivers(self):
        for currDriver in self.drivers:
            currDriver.quit()

        self.drivers = []

    def start_bot(self):
        try:
            print("starting Bot")

            for currDriver in self.drivers:
                currDriver.get(self.videosBot.get_next_video())

                # element = currDriver.find_element_by_xpath("//button[@aria-label='Play']")
                # print("element " + element)
                # if (element is not None):
                #     element.click()

            time.sleep(random.randint(360, 400))
            self.reset_drivers()
            self.start_bot()
        except:
            err = sys.exc_info()[0]
            print(str(err) + " Error occured")
            self.reset_drivers()
            self.start_bot()


