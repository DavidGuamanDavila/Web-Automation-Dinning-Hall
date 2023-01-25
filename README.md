# Web-Automation-Dinning-Hall-MUN
## Description
<p> This web automation project fills in the Box Lunch Order form of MUN's Dining Hall and submits it. </p>
<p> The project also sends you a confirmation email that the form was submitted. </p>

## Technology Stack
* Selenium was used to automate the browser.
* Python was used to access different libraries and fill out the form
* Chrome Developer tools were used to inspect the form and retrieve the Xpath and CSS selector

## Guidence

* You will need to install the following modules using pip install: selenium, sendgrid, and pyautogui
* To set your email to be able to receive the confirmation please fill the form with your email address: https://forms.gle/JNffJdoeU6cXW6qZ7
* You will recieve a verification link from SendGrid, please accept it (Please note it might take some time depending on our availability to set your account up)
* Until the email is set, feel free to comment out lines 137-163
* After your email is set, please do the following:
1- For Mac:
```
    1.1- Open a terminal
    1.2- type ```echo "export SENDGRID_API_KEY='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'" > sendgrid.env``` and press enter
    1.3- type ```echo "sendgrid.env" >> .gitignore``` and press enter
    1.4- type ```source ./sendgrid.env``` and press enter
    1.5- Restart your IDE
```
2- For Windows:
```
    2.1- Type in your search cmd and press enter 
    2.2- type ```setx SENDGRID_API_KEY "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"``` and press enter
    2.3- Restart your IDE
```

