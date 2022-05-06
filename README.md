## eCommerce App testing

This is the test automation framework which aims at automating 
web-application with the help of python programming language
for GUI automation using POM(PageObjectModel).
The folder structure for the framework is defined as below.

- Configurations - it contains login details like URL, username and password details in .ini file

- Logs - This folder contains logs

- PageObjects --> this page contains Modules which contains
page information in class . Each class contains locators and
actions related to the Page. This helps in maintaining the code 
easily and improves code reusability.

- Reports -- this folder contains report.html which will showcase
how many test cases are passed,failed and skipped

- Screenshots- contains screenshots of test runs

- TestCases -- This folder contains test cases for the application under test

- TestData -- folder contains different combinations of input parameters for test cases

- utilities -- contains reusable code for writing the test cases.
this helps in reusing a code in multiple modules.




