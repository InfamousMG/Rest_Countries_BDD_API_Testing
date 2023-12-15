# Rest Countries API Testing with BDD approach #

This project has been created in order to test some of the endpoints of REST Countries API with the use of BDD approach. 
I have developed this project as a part of my portfolio as a Quality Control Engineer.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)


## General info
The documentation of the API is located here: https://restcountries.com/

To introduce Behavior-Driven Development, I make use of Behave framework together with Gherkin language to write natural-language-styled test scenarios. 
Python's Requests library is utilized to operate API calls and Allure is a tool used to build reports.
Also, to be able to apply BDD, PyCharm in professional edition is required (Pycharm community version does not support BDD).

## Technologies
Project is created with:
- Python 3.11
- Requests 2.28.2
- Behave 1.2.6
- Allure-Behave 2.13.2
- PyCharm professional 2023.2.5
- Allure-commandline 2.13.8

## Setup
In order to run the project, install all the above-mentioned technologies on your local machine.

Then, clone the repository from GitHub https://github.com/InfamousMG/Rest_Countries_BDD_API_Testing

## Usage
- To trigger all scenarios at once, run 'behave' in the terminal.
- To trigger particular scenarios marked with tags, run 'behave --tags=<scenario tag>'
- To trigger scenarios with print statements, run 'behave --no-capture'
- To create a report in Allure, run 'behave -f allure_behave.formatter:AllureFormatter -o AllureReports'. In AllureReports folder, there is an example of a report with a screenshot of html version opened in a browser
- To view the Allure report in a browser (html format), navigate to a directory where your 'allure-commandline-2.13.8\allure-2.13.8\bin' is located and run 'allure serve <location of your Allure Report>'