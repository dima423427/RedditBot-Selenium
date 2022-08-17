from socket import timeout
from urllib import response
import praw
import enchant
import time

##########################ДЛЯ РАБОТЫ С ЭКСЕЛЕМ
import pandas as pd

##########################ДЛЯ РАБОТЫ С ПРОКСИ
import requests
from bs4 import BeautifulSoup

##########################SELENIUM
from selenium import webdriver
import time 
import os

##########################МУЛЬТПОТОК
import threading

'''
#АВТОРЕГ                                   КАПЧАААААААААААААААААААААААААААААААААА
options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(options=options)
driver.get('https://www.reddit.com/register/')

Input_Email = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input[2]").send_keys("pixeldraw_io@mail.ru")
time.sleep(1) 
Submit_Email = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/button").click() 
time.sleep(1)
Input_UserName = driver.find_element_by_xpath("//*[@id='regUsername']").send_keys("*********")
time.sleep(1) 
Input_Password = driver.find_element_by_xpath("//*[@id='regPassword']").send_keys("*********")
time.sleep(3) 
Capcha = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click() 
time.sleep(2)
Submit = driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div/div[3]/button").click() 
time.sleep(2)
'''

'''
####################БЕРУ ДАННЫЕ ИЗ БД
# Load the xlsx file
excel_data = pd.read_excel('C:\\БД.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['title', 'link'])
# Print the content
print("The content of the file is:\n", data)
####################БЕРУ ДАННЫЕ ИЗ БД
'''

####################БЕРУ ДАННЫЕ ИЗ БД
excel_data = pd.read_excel('C:\\Авторизация.xlsx')

'''
data_login = pd.DataFrame(excel_data, columns=['username'])
data_password = pd.DataFrame(excel_data, columns=['password'])
print("The content of the file is:\n", data_login, data_password)
'''

login = excel_data.iloc[0,4]
passw = excel_data.iloc[0,2]
####################БЕРУ ДАННЫЕ ИЗ БД

#АВТОВХОД
options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(options=options)
driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

entername = driver.find_element_by_id("loginUsername")
entername.send_keys(login) #ВВОД ЛОГИНА

time.sleep(2)

enterpw = driver.find_element_by_id("loginPassword")
enterpw.send_keys(passw) #ВВОД ПАРОЛЯ

time.sleep(1) 

p_loginl = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click() 

time.sleep(10) 


########ПОСТИНГ
def Posts():
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.push.enabled", False)
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.reddit.com/')

close_window = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div[1]/div[2]/button").click() 
time.sleep(1) 
create_post = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div[2]/div/div[1]/span[3]/button").click() 
time.sleep(1)  
Title_Text = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea").send_keys("Тест1") 
time.sleep(1) 
Title_Text_Main = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div").send_keys("Тест1") 
time.sleep(1)
Drop_List = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/i").click()  
time.sleep(1)
Subreddit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input").send_keys("u/negativnie")
time.sleep(1)
Title_Text_Main = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div").click() 
time.sleep(6) ##ТУПО ДЛЯ СМЕНЫ КУРСОРА
Submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button").click() 
time.sleep(6)

'''
##РАБОТА С ПРОКСИ
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

proxies = {
  'https': 'http://51.77.159.133:80'
}

def get_location(url):
  response = requests.get(url=url, headers=headers, proxies=proxies)
  soup = BeautifulSoup(response.text, 'lxml')

  ip = soup.find('div', class_='ip').text.strip()
  location = soup.find('div', class_= 'value-country').text.strip()

  print(f'IP: {ip}\nLocation: {location}')



def main():
  get_location(url='https://2ip.ru')

if __name__ == '__main__':
  main()
'''

####РАБОТА С ПОТОКАМИ
t1 = threading.Thread (target=Posts)
t2 = threading.Thread (target=Posts)
t1.start()
t1.start()
