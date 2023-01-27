from selenium import webdriver
import time
from datetime import datetime, timedelta
import schedule
import smtplib
from email.mime.text import MIMEText
import base64
import pyautogui
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




#Open chrome browser
web = webdriver.Chrome()
web.get('https://forms.office.com/Pages/ResponsePage.aspx?id=D59Rsb8tIU6_NKaGzpdYioIz-RoWPs5FoBoJAop9UFdUNEcxNlJETVI2U0I4VksxWDRWWjZPVUlFOC4u')

time.sleep(2)
FirstName = "Fill in"
first = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/textarea')
first.send_keys(FirstName)

time.sleep(2)
LastName = "Fill in"
last = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/textarea')
last.send_keys(LastName)


time.sleep(2)
StudentId = "Fill in"
studentid = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/textarea')
studentid.send_keys(StudentId)

time.sleep(2)
Phone = "Fill in"
phone = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/textarea')
phone.send_keys(Phone)

time.sleep(2)
Email = "Fill in"
email = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/textarea')
email.send_keys(Email)

time.sleep(2)
agree_btn = web.find_element("xpath", '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div/div/label/input')
agree_btn.click()


time.sleep(2)
#Format: mm/dd/YYYY
#automatically run the code
#date_tmr = datetime.now() + timedelta(1)
#Date = date_tmr.strftime('%m/%d/%Y')
Date = "Fill in"
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
    filePath = '[Add your own path of a .png image]'
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(filePath)
    sender = ("[add your email]")
    recipients = ("[add your email]")
    subject = "Dining Hall Confirmation"
    body = "The form has been sent successfuly. Please find the attached image"
    with open(filePath, 'rb') as f:
        data = f.read()
        f.close()
    png = base64.b64encode(data).decode()

    image = MIMEImage(data, name=os.path.basename(filePath))


    msg = MIMEMultipart(body)

    msg.attach(image)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    smtp_server = smtplib.SMTP_SSL('mail.smtp2go.com', 465)
    smtp_server.login("DhallAutoForm", "DhallAuto2023")
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
    
else:
    print("The test was not succesful")
