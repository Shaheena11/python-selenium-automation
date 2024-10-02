
Feature: Window Handling

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open main page
    When Click on Sign In
    Then From right side navigation menu click Sign In
    And Verify Sign In form opened
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
