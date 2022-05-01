import logging
from os import environ

import pandas as pd

from typing import List
from dataclasses import dataclass, field

from more_itertools import chunked

from pytrends.request import TrendReq
from google_trends_scraper.models.input_arguments import InputArguments

LOGGER = logging.getLogger(__doc__)
logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))


@dataclass
class ScraperInterface:
    """ Class abstraction on top of the unofficial API for GoogleTrends.
    Notes:
        PyTrends homepage: https://github.com/GeneralMills/pytrends
    """

    _TIME_FRAME = 4
    _KEY_WORDS_QUOTA_PER_REQUEST = 5
    # Until we would like to apply any modifications over response format
    # response_hash_table: List[GoogleTrendsAPIResponse] = field(default_factory=lambda: [])

    arguments: InputArguments
    # by default, interface does not hold any KeyWords
    key_words: List = field(default_factory=lambda: [])

    connector: TrendReq = None
    timeout: range = (10, 25)
    retries: int = 3
    backoff_factor: int = 0.1

    def setup_connector(self):
        self.connector = TrendReq(hl=self.arguments.host_language,
                                  tz=self.arguments.time_zone,
                                  timeout=self.timeout,
                                  retries=self.retries,
                                  backoff_factor=self.backoff_factor)
        return self

    def get_search_interest_score(self) -> pd.DataFrame:
        """ Function which chunk-wise pulls interest score in requested time-frame.
        Notes:
            can employ async invocations trough @async decorator
        """

        search_over_time = pd.DataFrame()
        for chunk in chunked(self.key_words, self._KEY_WORDS_QUOTA_PER_REQUEST):
            try:
                response = self.connector.get_historical_interest(keywords=chunk,
                                                                  year_start=self.arguments.start_year,
                                                                  year_end=self.arguments.end_year,
                                                                  month_start=self.arguments.start_month,
                                                                  month_end=self.arguments.end_month,
                                                                  day_start=self.arguments.start_day,
                                                                  day_end=self.arguments.end_day,
                                                                  hour_start=self.arguments.start_hour,
                                                                  hour_end=self.arguments.start_hour + self._TIME_FRAME)

                response.drop(columns=['isPartial'], inplace=True)
                search_over_time = pd.concat([search_over_time, response], axis=1)

            except Exception as e:
                LOGGER.info(f'Failed to pull keywords: {chunk} with exception: {e}')
                continue

        return search_over_time
