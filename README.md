Selene+pytest+allure sample
========================

This is a sample project to practice selenide-pytest-allure integration
 
 # How to run:
 You need dependencies from requirements.txt and allure cli installed
 
 To run tests you need run following commands:
  
  1. ``` py.test --alluredir allure-report ```
  2. ``` allure generate allure-report -o target ```
  
  Open target/index.html in firefox to see allure report
  
  
  Alternative: run 'run.py'
  
  # Additional information:
  
  1. To run tests in different browser set 'selene_browser_name' environmental variable (Chrome is default)
  2. To run specific story add --allure_stories='comma_separated_stories_list'
  2. To run specific priority add --allure_severities='comma_separated_severities_list'
  
  # TODO:
  
   - replace requirements.txt(pip + virtualenv) with pipenv
   - ? move verification + make common allure-step function?
   - selene/config env variables in command line
