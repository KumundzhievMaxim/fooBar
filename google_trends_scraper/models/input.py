import pandas as pd
from pydantic import BaseModel, validator


class CSVInputFormat(BaseModel):
    dataframe: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True

    @validator('dataframe')
    def validate_key_words_is_df_column(cls, value):
        """ True if Series column name is 'KeyWords', otherwise False.
        Notes:
            columns name is set and controlled in main.InputReader interface.
        """

        columns = value.columns.values

        if len(columns) != 1 or columns[0] != 'KeyWords':
            raise TypeError('Input CSV file does not match input format.')

        return value

    @validator('dataframe')
    def validate_df_is_not_empty(cls, value):
        """ True if Series/DataFrame is entirely empty (no items), meaning any of the axes are of length 0. """
        return value if value.empty is False else TypeError('Input CSV file does not hold any values.')

    # @validator('dataframe')
    # def validate_key_words_isalpha(cls, value):
    #     """ @TODO double check with the customer what exactly we expect as row value in KeyWords. """
    #     return value if all(value['KeyWords'].str.isalpha()) is True else \
    #         TypeError('Input CSV file holds rows which do not match with expected format.')

