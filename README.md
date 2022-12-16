Selene+pytest+allure sample
========================

This is a sample project with selenide-pytest-allure integration
 
 # How to run:
 You need dependencies from requirements.txt and allure cli installed
 
 To run tests and see report you need run following commands:
  
  1. ``` py.test --alluredir allure-report ```
  2. ``` allure generate allure-report -o target ```
  3. ``` allure serve allure-report ```
  
  Open target/index.html in firefox to see allure report
  
  # Additional information:
  
  1. To run tests in different browser set 'selene_browser_name' environmental variable (Chrome is default)
  2. To run specific story add --allure_stories='comma_separated_stories_list'
  2. To run specific priority add --allure_severities='comma_separated_severities_list'
