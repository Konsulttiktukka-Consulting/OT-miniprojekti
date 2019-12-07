Feature: List all videos

  Scenario: List videos
    Given I am at the start page
    When I click the video list button
    Then I am shown a list containing all videos
