Feature: Search functionallity
    # @completed
    Scenario: search for vaild product
        Given I got naviagted to home page 
        When Enter  valid product into the search box
        And click on search button 
        Then Vaild product should get displayed
    # @completed
    Scenario: search for INvaild product
        Given I got naviagted to home page 
        When Enter  INvalid product into the search box
        And click on search button 
        Then Proper meaasge should displayed on search button 

    @completed
    Scenario: Search without entering the Product 
        Given I got naviagted to home page 
        When DO not enter anything into the search box
        And click on search button 
        Then Proper meaasge should displayed on search button 
