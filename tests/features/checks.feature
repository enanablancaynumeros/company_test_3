Feature: Microservice is ok for sys admins

  Scenario: The microservice health is ok
      When the microservice is up and running
       Then the response of the microservice is "{"msg": "ok"}"
