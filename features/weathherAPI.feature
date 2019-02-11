
Feature: This feature is to check weather GET API sample
@api
Scenario: Check if user is able to submit GET API request and is getting the response
  Given user creates a api get service
   When user submits the GET request
   Then user validates the status code
