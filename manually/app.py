import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/search/results/all/?keywords=programação&origin=GLOBAL_SEARCH_HEADER&sid=WO5")
driver = webdriver.Chrome(options=options)

