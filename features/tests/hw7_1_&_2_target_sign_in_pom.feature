
Feature: Target Sign-in Functionality

  Scenario: User can sign in to target
    Given Open main page
    When Click on Sign In
    Then From right side navigation menu click Sign In
    And Verify Sign In form opened

  Scenario: User Can Search for a Product and add it to the cart
    Given Open main page
    When Search Coffee
    Then Click on Add to Cart Button

