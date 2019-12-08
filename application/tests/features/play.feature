Feature: Play

  Scenario: Watch youtube video
    Given I am at the start page
    When I click the video list button
    Then I can see a added youtube video in embedded form

  Scenario: Watch twitch stream
    Given I am at the start page
    When I click the video list button
    Then I can see a added twitch stream in embedded form

    
