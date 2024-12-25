Feature: Login functionallity
    @login
    Scenario: Login with valid credentials
        Given I naviagted to Login page 
        When Enter  valid Email And Vaild Password 
        And click Login button 
        Then Login successfull
    @login
    Scenario: Login with invalid Email and Valid Password
        Given I naviagted to Login page 
        When Enter Invalid Email and vaild password
        And click Login button 
        Then Proper Warning message displayed

    @login
    Scenario: Login with valid Email and INValid Password
        Given I naviagted to Login page
        When Enter valid Email and INvaild password
        And click Login button 
        Then Proper Warning message displayed
    @login
    Scenario: Login with Invalid credentials
        Given I naviagted to Login page
        When Enter INvalid Email and INvaild password
        And click Login button 
        Then Proper Warning message displayed
