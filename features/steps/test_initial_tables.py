import numpy as np
import pandas as pd
import pyarrow.parquet as pq

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pytest_bdd.parsers import parse
from pandas.testing import assert_frame_equal

folder_path = "data/"
df_db = ""


@scenario("../initial_tables.feature", "Validate row count and columns match with the test data")
def test_intial_tables():
    pass


@given("I have successfully connected to the SQL database")
def connect_db():
    pass


@given(parse("I have {input_file} data for the equivalent {table}"))
def find_data(input_file, table):
    pass


@given("I have upload the data into database")
def upload_data():
    pass


@given("I run the migration code")
def run_migration():
    pass


@when(parse("I fetch all the rows from the {table}"))
def fetch_data(table):
    global df_db
    df_db = pd.read_csv(folder_path + table + '.csv')
    df_db['cr_date'] = pd.to_datetime(df_db['cr_date'])


@then(parse("the {table} output result should match with {expected_file} data"))
def validate_data(table, expected_file):
    df_expected = pq.read_table(source=folder_path + 'expected_data/' + expected_file).to_pandas()
    df_expected.replace(to_replace=[None], value=np.nan, inplace=True)

    assert_frame_equal(df_db, df_expected)
