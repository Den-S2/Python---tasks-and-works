# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
# try:
#     drriver.get(url='https://www.marvel.com/')
#     # time.sleep(3)
#     name = drriver.title
#     elements1 = drriver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]/div/ul/div[@class="mvl-card mvl-card--feed"]/div/div/p[2]/a''')
#     href_s = [i.get_attribute("href") for i in elements1]
#     for i in range(len(href_s)):
#         drriver.get(href_s[i])
#         drriver.get_screenshot_as_file(f'{i}.png')
# except Exception as error:
#     print(error)
# finally:
#     drriver.close()
#     drriver.quit()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
# try:
#     ask = input("Enter name file: ")
#     file = open(ask + ".txt", "w")
#     drriver.get(url='https://www.marvel.com/characters')
#     # time.sleep(3)
#     name = drriver.title
#     elements = drriver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
#     elements1 = drriver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a/div[2]/p''')
#     href_s = [i.get_attribute("href") for i in elements]
#     for i,j in zip (elements1, href_s):
#         file.write(i.text + " : " + j + "\n")
#     file.close()
# except Exception as error:
#     print(error)
# finally:
#     drriver.close()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"/Selenium\chromedriver.exe")
try:
    drriver.get(url='https://www.marvel.com/characters')
    # time.sleep(3)
    name = drriver.title
    elements = drriver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
    href_s = [i.get_attribute("href") for i in elements]
    for i in range(len(href_s)):
        drriver.get(href_s[i])
        drriver.get_screenshot_as_file(f'{i}.png')
except Exception as error:
    print(error)
finally:
    drriver.close()