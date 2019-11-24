Feature: list all books

  Scenario: List books
    Given I am at the start page
    When I click the book list
    Then I am shown a list containing all books