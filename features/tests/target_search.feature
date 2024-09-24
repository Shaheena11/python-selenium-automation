Feature: Tests for Target Search functionality

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct search results shown for coffee

  Scenario: User can search for tea
    Open Target main page
    When Search for tea
    Then Verify that correct search results shown for tea

  Scenario Outline:
    Given Open Target main page
    When Search for <search_word>
    Then Verify that correct search shown for <search_result>
    Examples:
    |search_word |search_result |
    |coffee      |coffee        |
    |tea         |tea           |
    |mug         |mug           |
    |Sugar       |sugar         |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from the side navigation
    And Open cart page
    Then Verify cart has 1 item
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image
