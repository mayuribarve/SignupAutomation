# Created by mayurib at 11/27/2017

Feature: sign up to Borland Insurance site
  # In order to ensure Login Functionality works,
  # I want to run the test to verify it is working


  Scenario: Open Borland website
    Given User opens Borland website
    Then  print the title
    And Signup option is available


  Scenario: User navigates to Sign up page
    Given User is on borland home page
    When User selects Sign up option
    Then User should see Sign up page


  Scenario: User enters account information
    Given User is on Sign up page
    When User enters First Name
    And User enters Last Name
    And User enters Birthdate
    And User enters Email address
    And User enters Mailing address
    And User enters City
    And User selects State
    And User enters Postal code
    And User enters password
    And User clicks SIGN UP button
    Then User should be signed up successfully

