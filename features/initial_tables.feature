Feature: Validate initial base tables - load csv files to database, read data from db and validate

  Background:
    Given I have successfully connected to the SQL database

  Scenario Outline: Validate row count and columns match with the test data
    Given I have <input_file> data for the equivalent <table>
    And I have upload the data into database
    And I run the migration code
    When I fetch all the rows from the <table>
    Then the <table> output result should match with <expected_file> data
    Examples:
      | table        | input_file       | expected_file        |
      | first_table  | first_table.csv  | first_table.parquet  |
      | second_table | second_table.csv | second_table.parquet |