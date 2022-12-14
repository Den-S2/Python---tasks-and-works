from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
try:
    drriver.get(url='https://lardi-trans.ua/ru/gruz/'); time.sleep(2)
    count = 0
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    ele_country = drriver.find_element(By.XPATH, '''//*[@id="react-select-2-input"]''')
    ele_city = drriver.find_element(By.XPATH, '''//*[@id="react-select-4-input"]''')
    ele_country1 = drriver.find_element(By.XPATH, '''//*[@id="react-select-6-input"]''')
    ele_city1 = drriver.find_element(By.XPATH, '''//*[@id="react-select-8-input"]''')
    ele_country.send_keys(input("Enter country: "), Keys.ENTER); time.sleep(0.1)
    ele_city.send_keys(input("Enter city: ")); time.sleep(1)
    ele_city.send_keys(Keys.ENTER)
    checker = input("You want add destination way? Print yes/no: ")
    if checker == "yes":
        ele_country1.send_keys(input("Enter destination country: "), Keys.ENTER); time.sleep(0.1)
        ele_city1.send_keys(input("Enter destination city: ")); time.sleep(1)
        ele_city1.send_keys(Keys.ENTER)
    else:
        print("Okay!")
    drriver.find_element(By.XPATH, '''//*[@id="proposal-search"]/div/div/div[3]/div[2]/button/span''').click(); time.sleep(3)
    print(drriver.find_element(By.XPATH, '//*[@id="proposal-search"]/div/div/div[3]/div[2]/div/p').text); time.sleep(1)
    while True:
        time.sleep(5)
        ele_cargo_tru = drriver.find_elements(By.XPATH, '//div[@class="ps_data ps_search-result_data-cargo ps_data-cargo"]/div/span[1]/span')
        ele_cost_tru = drriver.find_elements(By.XPATH, '//div[@class="ps_data ps_search-result_data-payment ps_data-payment"]/span[1]')
        for elements in range(len(ele_cost_tru)):
            print(ele_cargo_tru[elements].text, ele_cost_tru[elements].text)
            file.write(f'{ele_cargo_tru[elements].text}- {ele_cost_tru[elements].text}')
        time.sleep(1)
        drriver.find_element(By.XPATH, '//a[contains(@rel,"next")]').click()
        time.sleep(3)
    file.close()
except Exception as error:
    print(error)
finally:
    drriver.close()
