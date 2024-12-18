import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

df = pd.read_excel("D://UCL.xlsx", na_values=['NA'], usecols="A,B,C,D,E") 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.rapidtables.com/tools/notepad.html")

for index, row in df.iterrows():
    ranking = row[0]
    clubname = row[1]
    ucltitles = row[2]
    lastwon = row[3]
    opponent = row[4]
    
    time.sleep(1)

    area = driver.find_element(By.ID,"area")
    area.send_keys(ranking,'  ||  ',clubname,'  ||  Number of titles: ',ucltitles,'  ||  Last won on ',lastwon,'  ||  Won against ',opponent)
    
    



driver.quit()

