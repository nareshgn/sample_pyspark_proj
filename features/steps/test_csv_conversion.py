import os
from pathlib import Path

import pandas as pd
import glob
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

folder_path = "data/convert_to_csv/"
filenames = ""


@scenario("../convert_csv.feature", "Apply rules to generate custom csv double pipe separator")
def test_convert_csv():
    pass


@given("I have standard csv files at the source location")
def csv_source():
    global filenames
    file_location = os.path.join(folder_path, 'sample_data.xlsx')
    filenames = glob.glob(file_location)


@when("the conversion rules is applied on all the files")
def apply_rules():
    global filenames
    for file in filenames:
        df = pd.read_excel(file)
        df = df.replace(['NULL'], '')

        file_name = Path(file).stem
        df.to_csv(folder_path + file_name + '.csv', encoding='utf-8', index=False, header=True)

        file_in = open(folder_path + file_name + '.csv', 'rt')
        # output file to write the result to
        file_out = open(folder_path + file_name + '_formatted.csv', "wt")
        for line in file_in:
            # read replace the string and write to output file
            file_out.write(line.replace(',', '||'))
        # close input and output files
        file_in.close()
        file_out.close()


@then("I should be see custom csv files generated in the target location")
def check_csv_output():
    file_path = os.path.join(folder_path, '*_formatted.csv')
    output_files = glob.glob(file_path)
    assert len(output_files) > 0, "Failed to convert to custom CSV format"
