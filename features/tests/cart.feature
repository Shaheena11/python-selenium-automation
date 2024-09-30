
Feature: Cart tests

  Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown
