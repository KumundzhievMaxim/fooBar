
import pandas as pd

from dataclasses import dataclass, field
from pydantic_cli import run_and_exit

from google_trends_scraper.models.input_arguments import InputArguments
from google_trends_scraper.models.input import CSVInputFormat

"""
repeat in N hours
for each keyword:  
    scrape the api
        get the api response
        validate the api response
    dump results to the local destination (think about output structure) 
"""


@dataclass
class InputReader:
    dataframe: CSVInputFormat = field(default=pd.DataFrame)
    input_source_location: str = field(default=None)
    set_input_file_column_name: str = 'KeyWords'
    set_input_file_header_name: str = None

    def read_csv(self):
        """ Function which reads just csv file. """

        input_csv_to_validate = pd.read_csv(self.input_source_location,
                                            header=self.set_input_file_header_name,
                                            names=[self.set_input_file_column_name])

        self.dataframe = CSVInputFormat(dataframe=input_csv_to_validate)
        return self


@dataclass
class GoogleTrendsInterface:
    passs


def main(arguments: InputArguments) -> int:
    """ Main interface entrypoint. """

    dataframe = InputReader(input_source_location=arguments.source_input_location).read_csv().dataframe
    print(type(dataframe))
    return 0


if __name__ == "__main__":
    run_and_exit(InputArguments, main, description=__doc__, version="0.1.0")
