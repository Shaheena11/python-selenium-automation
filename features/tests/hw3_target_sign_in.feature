# Created by Shaheena at 9/12/24
Feature: Tests for Target Search functionality

  Scenario: User can see sign in form opened
   Given Open target page
   When Click Sign In
   Then From right side, click Sign In
   Then Verify sign in Target account