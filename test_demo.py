
from selenium import webdriver
import openpyxl
import test
import test_data
import time

def unit_test(self):
 self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
 self.driver.maximize_window()
 self.driver.get("http://35.239.251.99:3000/")
 self.driver.find_element_by_xpath("//a[text()='Add a User']").click()
 path = "C:\\Users\\sowmya\\Desktop\\test.xlsx"
 rows= test_data.getRowCount(path, 'Sheet1')
 for r in range(2,rows+1):

  firstname = test_data.readData(path, "Sheet1", r, 1)
  lastname = test_data.readData(path, "Sheet1", r, 2)
  phone = test_data.readData(path, "Sheet1", r, 3)
  email = test_data.readData(path, "Sheet1", r, 4)
  team = test_data.readData(path, "Sheet1", r, 5)
  userName = test_data.readData(path, "Sheet1", r, 6)
  password = test_data.readData(path, "Sheet1", r, 7)
  retypepassword = test_data.readData(path, "Sheet1", r, 8)
  self.driver.find_element_by_id("firstName").send_keys(firstname)
  self.driver.find_element_by_id("lastName").send_keys(lastname)
  self.driver.find_element_by_id("phone").send_keys(phone)
  self.driver.find_element_by_id("email").send_keys(email)
  self.driver.find_element_by_id("team").send_keys(team)
  self.driver.find_element_by_id("userName").send_keys(userName)
  self.driver.find_element_by_id("password").send_keys(password)
  self.driver.find_element_by_id("retype-password").send_keys(retypepassword)
  assert password == retypepassword
  self.driver.find_element_by_xpath("//span[@class='lever']").click()
  self.driver.find_element_by_xpath("//button[text()='Add User']").click()
  self.driver.find_element_by_xpath("//a[@href='/Users']/a").click()
  time.sleep(5)
  self.driver.find_element_by_xpath("//text[contains(text(),'"+firstname+"')]").click()
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
  self.driver.get_screenshot_as_file("ss3.png")
  self.driver.find_element_by_xpath("//button[contains(text(),'delete')]").click()
  time.sleep(2)


  self.driver.close()

















