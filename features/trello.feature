Feature: Trello

  Scenario: Adding Trello cards
    Given I have created a Trello board with three cards
    Then I can see the three cards on the Trello board

  Scenario: Editing a Trello card
    Given I have created a Trello board with three cards
    When I edit a Trello card
    Then I can see the Trello card has been updated
    
  Scenario: Deleting a Trello card
    Given I have created a Trello board with three cards
    When I delete a Trello card
    Then I can see the Trello card has been deleted

  Scenario: Adding a comment to a Trello card (API)
    Given I have created a Trello board with three cards
    When I add a comment to a Trello card
    Then I can see the comment on the Trello card

  Scenario: Adding a comment to a Trello card (Browser)
    Given I have created a Trello board with three cards
    When I add a comment to a Trello card using the browser
    Then I can see the comment has been added to the Trello card

  Scenario: Set the Trello card to done
    Given I have created a Trello board with three cards
    When I set the Trello card to done
    Then I can see the Trello card is done

  Scenario: Login error message
    Given a browser
    When I visit "https://trello.com/login"
    And I fill in "user" with "this is not my username"
    And I press "Log in"
    Then I should see there is no account for this username error message
