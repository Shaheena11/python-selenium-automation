# Created by Shaheena at 9/11/24
Feature: Tests for Target Search functionality

  Scenario: User can see that cart is empty
    Given Open target page
    When Click on Cart icon
    Then Verify that cart is empty