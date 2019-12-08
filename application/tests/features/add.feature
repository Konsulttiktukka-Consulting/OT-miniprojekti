Feature: Add

  Scenario: Navigate to add to video
    Given I am at the start page
    When I click the add video button
    Then I am shown a form to add a video

  Scenario: Post a new youtube video
    Given I am at the add video page
    When I enter a valid youtube url and submit the form 
    Then The video is added and shown in the video list

  Scenario: Post a new twitch stream
    Given I am at the add video page
    When I enter a valid twitch url and submit the form 
    Then The stream is added and shown in the video list
    
