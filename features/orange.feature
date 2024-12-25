Feature: OrangeLogin Feature

    Scenario Outline: Scenario Outline name: Orange check login test cases
        Given chrome driver launch
        When Enter valid credential '<username>' and '<password>' valuesss
        Then Varify logo

        Examples:
            | username | password |
            | Admin | admin123 |
            | Admin | admin123 |
