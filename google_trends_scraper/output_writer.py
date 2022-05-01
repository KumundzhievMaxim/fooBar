
from datetime import datetime

from dataclasses import dataclass

import pandas as pd

from google_trends_scraper.models.input_arguments import InputArguments


@dataclass
class LocalDriver:
    """ Format of outfile name: {destination}/{timestamp}_{keywords_selection_identifier}_{file_name}.{extension} """
    arguments: InputArguments
    keywords_selection_identifier: str = 'toy_sample'
    file_name: str = 'search_interest_score'
    file_extension: str = 'csv'
    tag_file_timestamp: str = datetime.utcnow()

    def write(self, material_to_write: pd.DataFrame) -> None:
        """ Function which writes dataframe to local machine. """
        file_name_destination = f'{self.arguments.source_output_location}/{self.tag_file_timestamp}_{self.keywords_selection_identifier}_{self.file_name}.{self.file_extension}'
        material_to_write.to_csv(file_name_destination)

        return





