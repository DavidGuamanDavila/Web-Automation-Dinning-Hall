# Web-Automation-Dining-Hall-MUN
## Description
This project automates the process of filling out and submitting the Box Lunch Order form for MUN's Dining Hall. It also includes a feature to send a confirmation email upon successful submission of the form.

## Technology Stack
* Selenium: Used for automating web browser interaction.
* Python: The primary programming language for script development.
* Chrome Developer Tools: Utilized for inspecting the web form and retrieving Xpath and CSS selectors.
## Guidance
### Prerequisites
* Python: Ensure you have Python installed on your machine.
* Web Browser: Google Chrome is required for this project.
### Installation
1. Clone the Repository: Download the project files from the repository.
2. Install Required Modules: Use pip to install necessary Python modules:
``` bash
pip install selenium sendgrid pyautogui
```
### Configuration
- Email Setup:
  - Fill out the provided form with your email address: Email Setup Form.
  - You will receive a verification link from SendGrid. Please verify your email.
  - It may take some time to set up your account, depending on our availability.
  - If your email is not set up yet, you can comment out lines 137-163 in the script.

## Running the Script
### Steps to Execute the Script
1. *Open Terminal or Command Prompt*: Navigate to the folder where you have saved the script.

2. *Set Script Parameters*: Before running the script, ensure that you have filled in your personal information in the script's placeholder fields (e.g., FirstName = "Fill in", etc.).

3. *Run the Script*: Execute the script by typing the following command in your terminal or command prompt:

``` bash
python3 DhallAutomationMUN.py
```


## What to Expect
- *Browser Automation*: Upon running the script, a browser window will open, and you will see the automated process of filling out the form.
- *Email Confirmation*: If everything is set up correctly, you should receive an email confirmation after the form is submitted.

### Note
- The script is configured to fill in default values for testing. Replace these with actual data where necessary.
- Follow the instructions within the script for further details on customizing your form submission.

## Additional Notes
- *Script Customization*: You can customize the script further to suit different forms or add additional functionality.

- *Automation Ethics*: Remember to use this script responsibly and in compliance with the terms of service of the website you are automating.

