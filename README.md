# bruteForceAttack
Automated Login Script Using Selenium

This Python script automates the process of logging into the Sauce Demo website using credentials from a text file. The script leverages Selenium WebDriver to simulate user actions such as entering a username and password, and submitting the login form.

#Features:
Reads credentials from a file: Automatically tries multiple username/password combinations stored in a text file (pass.txt).
Automates browser interaction: Uses Selenium WebDriver with Microsoft Edge to perform the login attempts.
Error Handling: Includes basic error handling to ensure the script continues running even if an error occurs during login.

#Requirements:
Python 3.x
Selenium
Microsoft Edge WebDriver

#Setup:
pip install selenium
Place your credentials (username/password combinations) in a file named pass.txt, with each combination on a new line.
Run the script to automate login attempts on https://www.yourwebsitename.com/.
