Feature: Makemytrip flight booking
    @mmt
    Scenario: Login with valid credentials
        Given I naviagted to MMT Home  page 
        When Select FROM option
        And Select To option 
        And Select Departure
        And click Search  button 
        Then Click on View Prices
