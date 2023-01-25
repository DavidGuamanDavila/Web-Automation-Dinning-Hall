from selenium import webdriver
import time
from datetime import datetime, timedelta
import schedule


#Open chrome browser
web = webdriver.Chrome()
web.get('https://forms.office.com/Pages/ResponsePage.aspx?id=D59Rsb8tIU6_NKaGzpdYioIz-RoWPs5FoBoJAop9UFdUNEcxNlJETVI2U0I4VksxWDRWWjZPVUlFOC4u')

time.sleep(2)
FirstName = "David"
first = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/textarea')
first.send_keys(FirstName)

time.sleep(2)
LastName = "Davila"
last = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/textarea')
last.send_keys(LastName)


time.sleep(2)
StudentId = "202014155"
studentid = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/textarea')
studentid.send_keys(StudentId)

time.sleep(2)
Phone = "7097256601"
phone = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/textarea')
phone.send_keys(Phone)

time.sleep(2)
Email = "adguaman@mun.ca"
email = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/textarea')
email.send_keys(Email)

time.sleep(2)
agree_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div/div/label/input')
agree_btn.click()


time.sleep(2)
#mm/dd/YYYY
Date = "01/24/2023"
date = web.find_element("xpath", '//*[@id="DatePicker0-label"]')
date.send_keys(Date)

time.sleep(2)
orderoption_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input')
orderoption_btn.click()

time.sleep(2)
lunch_entree_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[9]/div/div[3]/div/div[2]/div/label/input')
lunch_entree_btn.click()

time.sleep(2)
bread_type_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[10]/div/div[3]/div/div[6]/div/label/input')
bread_type_btn.click()

time.sleep(2)
prtn_type_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div[8]/div/label/input')
prtn_type_btn.click()

time.sleep(2)
cheese_type_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div[1]/div/label/input')
cheese_type_btn.click()

time.sleep(2)
lettuce_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[1]/div/label/input')
lettuce_btn.click()

time.sleep(1)
tomatoes_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[2]/div/label/input')
tomatoes_btn.click()

time.sleep(1)
cucumbers_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[3]/div/label/input')
cucumbers_btn.click()

time.sleep(1)
GP_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[4]/div/label/input')
GP_btn.click()

time.sleep(1)
RO_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[5]/div/label/input')
RO_btn.click()

time.sleep(1)
Olives_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div[7]/div/label/input')
Olives_btn.click()

time.sleep(2)
condiments_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[14]/div/div[3]/div/div[7]/div/label/input')
condiments_btn.click()

time.sleep(2)
lunch_side_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[15]/div/div[3]/div/div[1]/div/label/input')
lunch_side_btn.click()

time.sleep(2)
lunch_fruit_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[16]/div/div[3]/div/div[1]/div/label/input')
lunch_fruit_btn.click()


time.sleep(2)
lunch_dessert_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[17]/div/div[3]/div/div[3]/div/label/input')
lunch_dessert_btn.click()

time.sleep(2)
lunch_bvg_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[18]/div/div[3]/div/div[1]/div/label/input')
lunch_bvg_btn.click()


time.sleep(2)
submit_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[4]/div[1]/button/div')
submit_btn.click()


time.sleep(5)

#Validation of form submission
get_confirmation_div_text = web.find_element("css selector", '.thank-you-page-comfirm-text')
print(get_confirmation_div_text.text)

if ((get_confirmation_div_text.text) == "Thanks!"):
    print("The Test Was succesful")

else:
    print("The test was not succesful")
