# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
# try:
#     drriver.get(url='https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1670252714&rver=7.3.6960.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2frpsauth%2fv1%2faccount%2fSignInCallback%3fstate%3deyJSdSI6Imh0dHBzOi8vd3d3Lm1pY3Jvc29mdC5jb20vdWstdWEiLCJMYyI6IjEwNTgiLCJIb3N0Ijoid3d3Lm1pY3Jvc29mdC5jb20ifQ&lc=1058&id=74335&aadredir=0')
#     time.sleep(2)
#     count = 0
#     file = open("pass1.txt", "r")
#     password = file.read().split(); file.close()
#     ask = input("Enter name file: ")
#     file = open(ask + ".txt", "w")
#     ele_user = drriver.find_element(By.ID, "i0116")
#     ele_pass = drriver.find_element(By.ID, "password")
#     ele_user.send_keys(password[0])
#     ele_pass.send_keys(password[1])
#     time.sleep(1)
# except Exception as error:
#     print(error)
# finally:
#     drriver.close()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
drriver = webdriver.Chrome(executable_path=r"C:\Users\bleac\PycharmProjects\pythonProject\Selenium\chromedriver.exe")
try:
    drriver.get(url='https://lardi-trans.ua/gruz/')
    time.sleep(2)
    count = 0
    ask = input("Enter name file: ")
    file = open(ask + ".txt", "w")
    ele_country = drriver.find_element(By.XPATH, '''//*[@id="react-select-2-input"]''')
    ele_city = drriver.find_element(By.XPATH, '''//*[@id="react-select-4-input"]''')
    ele_country1 = drriver.find_element(By.XPATH, '''//*[@id="react-select-6-input"]''')
    ele_city1 = drriver.find_element(By.XPATH, '''//*[@id="react-select-8-input"]''')
    ele_country.send_keys(input("Enter country: "), Keys.ENTER)
    time.sleep(0.1)
    ele_city.send_keys(input("Enter city: "))
    time.sleep(1)
    ele_city.send_keys(Keys.ENTER)
    checker = input("You want add destination way? Print yes/no: ")
    if checker == "yes":
        ele_country1.send_keys(input("Enter destination country: "), Keys.ENTER)
        time.sleep(0.1)
        ele_city1.send_keys(input("Enter destination city: "))
        time.sleep(1)
        ele_city1.send_keys(Keys.ENTER)
    else:
        print("Okay!")
    drriver.find_element(By.XPATH, '''//*[@id="proposal-search"]/div/div/div[3]/div[2]/button/span''').click()
    time.sleep(3)
    print(drriver.find_element(By.XPATH, '//*[@id="proposal-search"]/div/div/div[3]/div[2]/div/p').text)
    time.sleep(1)
    count_list = drriver.find_element(By.CLASS_NAME, '''lrd-paginator__page ''')
    # if int(count_list.text) == 0:
    #     s = int(count_list.text) + 1
    #     print(s)
    # else:
    #     s = int(count_list.text) - 1
    #     print(s)
    # time.sleep(1)
    all_element = []
    while count != 1:
        ele_data_tru = drriver.find_elements(By.CLASS_NAME, '''ps_data.ps_search-result_data-cargo.ps_data-cargo''')
        # ele_data_tru = drriver.find_elements(By.XPATH, '//div[@class="ps_data ps_search-result_data-cargo ps_data-cargo"]/div/span[1]/span')
        ele_transport_tru = drriver.find_elements(By.CLASS_NAME, 'ps_data.ps_search-result_data-transport.ps_data-transport span')
        ele_cargo_tru = drriver.find_elements(By.CLASS_NAME, 'ps_data.ps_search-result_data-payment.ps_data-payment span')
        ele_cost_tru = drriver.find_elements(By.CLASS_NAME, 'ps_data_payment_info span')
        # date_block = [i.text for i in ele_data_tru]
        for i in ele_data_tru:
            all_element.append(i.text)
        tra_block = [i.text for i in ele_transport_tru]
        time.sleep(3)
        drriver.find_element(By.XPATH, '//a[contains(@rel,"next")]').click()
        time.sleep(3)
        count += 1
        print(all_element)
        # file.write(date_block + " - " + tra_block + "\n")
        for i in all_element:
            file.write(i + "\n")
    file.close()
except Exception as error:
    print(error)
finally:
    drriver.close()