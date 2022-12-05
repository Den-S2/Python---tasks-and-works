from selenium import webdriver
import time
from selenium.webdriver.common.by import By
drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
try:
    drriver.get(url='https://mystat.itstep.org/en/auth/login/index')
    time.sleep(2)
    count = 0
    file = open("pass.txt", "r")
    password = file.read().split(); file.close()
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    ele_user = drriver.find_element(By.ID, "username")
    ele_pass = drriver.find_element(By.ID, "password")
    ele_user.send_keys(password[0])
    ele_pass.send_keys(password[1])
    time.sleep(1)
    drriver.find_element(By.CLASS_NAME, 'login-action').click()
    time.sleep(5)
    drriver.get(url='https://mystat.itstep.org/en/main/schedule/page/index')
    time.sleep(5)
    actday = drriver.find_elements(By.CLASS_NAME, 'active-day')
    for day in actday:
        day.click()
        time.sleep(2)
        dayless = drriver.find_element(By.XPATH, '/html/body/modal-container/div/div/div/div[1]/h4')
        less = drriver.find_elements(By.CLASS_NAME, 'lessons')
        time.sleep(2)
        file.write(dayless.text + "\n")
        for lesson in less:
            file.write(lesson.text + "\n\n")
        time.sleep(0.5)
        drriver.find_element(By.XPATH,'/html/body/modal-container/div/div/div/div[1]/button/span').click()
        time.sleep(2)
    file.close()
except Exception as error:
    print(error)
finally:
    drriver.close()