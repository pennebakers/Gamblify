import undetected_chromedriver as uc
import time as time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_argument('proxy-server=106.122.8.54:3128')
options.add_argument('--user-data-dir=C:\\Users\\Seth Pennebaker\\AppData\\Local\\Google\\Chrome\\User Data\\Default')

browser = uc.Chrome(
    options=options
)

browser.get('https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1&SeasonType=Regular+Season')

time.sleep(5)

change = Select(browser.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select'))
change.select_by_index(0)

time.sleep(5)

rows = browser.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody')

Stats = []

print(rows.count)

#for row in rows:
 #   Stats.append(str(row.text))
    #print(row.text)

#column_names = ['Index', 'Player', 'Team', 'Age', 'GP', 'W', 'L', 'Min', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF', 'FP', 'DD2', 'TD3', '+/-']
#df = pd.DataFrame(data=rows, columns=column_names, index=False)
#df.set_index('Index')
#df.to_excel('stats.xlsx')

#cookies = browser.get_cookies()

#for playerNames in browser.find_elements(By.CLASS_NAME, 'Crom_text__NpR1_.Crom_primary__EajZu.Crom_stickySecondColumn__29Dwf'):
 #   print(playerNames.text)
    
#for playerTeams in driver.find_elements(By.CLASS_NAME, 'Crom_text__NpR1_'):
 #   print(playerTeams.text)

