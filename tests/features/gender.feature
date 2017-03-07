Feature: Get Gender

  Scenario: There are no messages consumed in the system and we request a client id gender
    When I ask for the gender of the client id 123
    Then the response is not ok and the error code is 404

  Scenario: There are messages consumed in the system and we request a client id gender that doesn't exists
    Given a message is consumed by the system with client id 1 and gender women
    When I ask for the gender of the client id 123
    Then the response is not ok and the error code is 404

  Scenario: There are messages consumed in the system and we request a client id gender with default heuristic
    Given a message is consumed by the system with client id 1 and gender man
    When I ask for the gender of the client id 1 with the default heuristic
    Then the response is ok and the gender is man