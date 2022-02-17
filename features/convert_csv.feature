Feature: Convert standard comma separated csv files to custom double pipe separator

  Scenario: Apply rules to generate custom csv double pipe separator
    Given I have standard csv files at the source location
    When the conversion rules is applied on all the files
    Then I should be see custom csv files generated in the target location