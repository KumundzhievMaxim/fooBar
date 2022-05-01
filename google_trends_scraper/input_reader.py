import pandas as pd

from dataclasses import dataclass, field
from google_trends_scraper.models.input import CSVInputFormat


@dataclass
class InputReaderInterface:
    table: pd.DataFrame = field(default=pd.DataFrame)
    input_source_location: str = field(default=None)
    set_input_file_column_name: str = 'KeyWords'
    set_input_file_header_name: str = None

    def read_csv(self):
        """ Function which reads just csv file. """

        input_csv_to_validate = pd.read_csv(self.input_source_location,
                                            header=self.set_input_file_header_name,
                                            names=[self.set_input_file_column_name])

        self.table = CSVInputFormat(dataframe=input_csv_to_validate).dataframe
        return self
