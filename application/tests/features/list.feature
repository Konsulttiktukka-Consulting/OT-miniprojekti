Feature: List

  Scenario: List videos and streams
    Given I am at the start page
    When I click the video list button
    Then I am shown a list containing all videos
