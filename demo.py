
from selenium import webdriver
import openpyxl
import data
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("http://35.239.251.99:3000/")
driver.find_element_by_xpath("//a[text()='Add a User']").click()
path = "C:\\Users\\sowmya\\Desktop\\test.xlsx"
rows= data.getRowCount(path,'Sheet1')
for r in range(2,rows+1):

    firstname = data.readData(path,"Sheet1",r,1)
    lastname = data.readData(path,"Sheet1",r,2)
    phone = data.readData(path,"Sheet1",r,3)
    email = data.readData(path, "Sheet1", r,4)
    team = data.readData(path, "Sheet1", r,5)
    userName = data.readData(path, "Sheet1", r,6)
    password = data.readData(path, "Sheet1", r,7)
    retypepassword = data.readData(path, "Sheet1", r,8)
    driver.find_element_by_id("firstName").send_keys(firstname)
    driver.find_element_by_id("lastName").send_keys(lastname)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("team").send_keys(team)
    driver.find_element_by_id("userName").send_keys(userName)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("retype-password").send_keys(retypepassword)
    assert password == retypepassword
    driver.find_element_by_xpath("//span[@class='lever']").click()
    driver.find_element_by_xpath("//button[text()='Add User']").click()
    driver.find_element_by_xpath("//a[@href='/Users']/a").click()
    time.sleep(5)
    driver.find_element_by_xpath("//text[contains(text(),'"+firstname+"')]").click()
    fullname = (firstname+" "+lastname)
    print("check if "+fullname+" contains "+firstname+"")
    print (firstname in fullname)
    time.sleep(2)
    assert userName == userName
    assert phone == phone
    assert email == email
    teams = "\r\n 1. developer \r\n 2. tester"
    currentteam = "tester"
    print("check if "+currentteam+" is in list of teams i.e " +teams+ "")
    print(currentteam in teams)
    driver.find_element_by_xpath("//button[contains(text(),'delete')]").click()
    time.sleep(2)


driver.close()
















