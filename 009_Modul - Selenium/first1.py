from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Atron\chromedriver.exe")
try:
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    drriver.get(url='https://www.marvel.com/')
    time.sleep(5)
    # drriver.get_screenshot_as_file("fablo.png")
    # drriver.save_screenshot("pablo.png")
    name = drriver.title
    # element = drriver.find_element(By.CLASS_NAME, "promo__title")
    # print(element.text)
    # elements =drriver.find_elements(By.CLASS_NAME, "feed__cards")
    # elements = drriver.find_elements(By.CLASS_NAME, "mvl-card__feed-wrapper")
    # elements = drriver.find_elements(By.CLASS_NAME, "card-body__headline")
    elements = drriver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]/div/ul/div[@class="mvl-card mvl-card--feed"]/div/div/p[1]''')
    elements1 = drriver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]/div/ul/div[@class="mvl-card mvl-card--feed"]/div/div/p[2]''')
    listd = []
    for i, j in zip(elements, elements1):
        file.write(i.text + " : " + j.text + "\n")
        listd.append(i.text)
        listd.append(j.text)
    print(listd)
    file.close()
except Exception as error:
    print(error)
finally:
    drriver.close()
    drriver.quit()