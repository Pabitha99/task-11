import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
# //*[@id="content"]/iframe
iframe_element=driver.find_element(By.XPATH,'//*[@id="content"]/iframe')
driver.switch_to.frame(iframe_element)
# source and destination elements
source_ele = driver.find_element(By.XPATH,'//div[contains(@class,"ui-widget-content") and contains(@class,"ui-draggable") and contains(@class,"ui-draggable-handle")]')
des_ele = driver.find_element(By.XPATH,'//div[contains(@class,"ui-widget-header") and contains(@class,"ui-droppable")]')
# drag and drop the rectangle
actions=ActionChains(driver)
actions.drag_and_drop(source_ele,des_ele).perform()


