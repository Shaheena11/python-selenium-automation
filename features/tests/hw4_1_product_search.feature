Feature: Test Scenarios for Target Search functionality

  Scenario: User can search for a product
    Given Open Target page
    When Input Mug into search field
    And Click on search icon
    Then Product results for Mug are shown