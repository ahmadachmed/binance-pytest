#!/bin/bash

# RUn test and generate allure-results
pytest --alluredir=./allure-results
# Generate HTML report
allure generate ./allure-results -o ./allure-report --clean
# Start allure to see the report
allure serve ./allure-results
