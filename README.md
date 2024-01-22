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
Copy code
``` bash
pip install selenium sendgrid pyautogui
```
### Configuration
- Email Setup:
  - Fill out the provided form with your email address: Email Setup Form.
  - You will receive a verification link from SendGrid. Please verify your email.
  - It may take some time to set up your account, depending on our availability.
  - If your email is not set up yet, you can comment out lines 137-163 in the script.
### Usage
- *Running the Script*: Execute the Python script to start the automation process.
- *Customizing the Form*: Modify the placeholders in the script (e.g., *FirstName = "Fill in"*) with your specific details.
### Note
- The script is configured to fill in default values for testing. Replace these with actual data where necessary.
- Follow the instructions within the script for further details on customizing your form submission.
