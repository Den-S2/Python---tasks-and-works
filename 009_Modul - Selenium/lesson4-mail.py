from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
try:
    drriver.get(url='https://outlook.office.com/mail/')
    time.sleep(2)
    count = 0
    file = open("pass1.txt", "r")
    password = file.read().split(); file.close()
    ele_user = drriver.find_element(By.ID, "i0116")
    ele_user.send_keys(password[0])
    time.sleep(2)
    drriver.find_element(By.ID, "idSIButton9").click()
    time.sleep(1)
    ele_pass = drriver.find_element(By.ID, "i0118")
    ele_pass.send_keys(password[1])
    time.sleep(1)
    drriver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    drriver.find_element(By.ID, "idBtn_Back").click()
    time.sleep(4)
    drriver.find_element(By.XPATH, '''//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/div/span/button[1]/span''').click()
    time.sleep(4)
    sendmess = drriver.find_element(By.XPATH, '''//*[@id="docking_InitVisiblePart_0"]/div/div[1]/div[1]/div/div[4]/div/div/div[1]''')
    sendmess.send_keys(input("Take mail or mails: "))
    time.sleep(1)
    sendtitle = drriver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/input")
    sendtitle.send_keys(input("Take title: "))
    time.sleep(1)
    sendtext = drriver.find_element(By.XPATH, '''//*[@id="editorParent_1"]/div/div''')
    sendtext.send_keys(input("Take text: "))
    time.sleep(1)
    drriver.find_element(By.XPATH, '''//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]/span''').click()
    time.sleep(3)
except Exception as error:
    print(error)
finally:
    drriver.close()