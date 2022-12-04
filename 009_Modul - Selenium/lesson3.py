from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
try:
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    drriver.get(url='https://www.marvel.com/characters')
    count = 0
    href_s, name_block = [], []
    while count != 1:
        ele_name = drriver.find_elements(By.XPATH,'''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a/div[2]/p''')
        ele_href = drriver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
        # for nna in ele_name:
        #     name_block.append(nna.text)
        name_block = [url.text for url in ele_name]
        # for url in ele_href:
        #     href_s.append(url.get_attribute("href"))
        href_s = [url.get_attribute("href") for url in ele_href]
        button = drriver.find_element(By.CLASS_NAME, 'pagination__item.pagination__item-nav.pagination__item-nav-next')
        button.click()
        time.sleep(3)
        count += 1
        for url in range(len(href_s)):
            drriver.get(href_s[url])
            time.sleep(3)
            ele_class = drriver.find_elements(By.XPATH,'''//*[@id="two_column-4"]/div/div[3]/div[1]/div[2]/div[2]/div/ul[@class="railBioInfo"]/li/p''')
            ele_bio = drriver.find_elements(By.XPATH,'''//*[@id="two_column-4"]/div/div[3]/div[1]/div[2]/div[2]/div/ul[@class="railBioInfo"]/li/ul/li''')
            file.write("\n" + name_block[url] + " : " + href_s[url] + "\n")
            for a, b in zip(ele_class, ele_bio):
                file.write(a.text + " - " + b.text + "\n")
except Exception as error:
    print(error)
finally:
    drriver.close()