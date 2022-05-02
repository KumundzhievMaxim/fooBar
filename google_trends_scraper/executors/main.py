import logging
from os import environ

from pydantic_cli import run_and_exit

from models.input_arguments import InputArguments

from interfaces.input_reader import InputReaderInterface
from interfaces.output_writer import LocalDriver

from interfaces.key_words_scraper import ScraperInterface

LOGGER = logging.getLogger(__doc__)
logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))


def main(arguments: InputArguments) -> int:
    """ Main interface entrypoint. """

    LOGGER.info('\n Job arguments: \n'
                f'{arguments} \n')

    key_words = InputReaderInterface(input_source_location=arguments.source_input_location).read_csv().table.values
    flat_key_words_list = [item for sublist in key_words for item in sublist]
    LOGGER.info('input csv file validated and loaded in-memory.')

    scraper = ScraperInterface(arguments=arguments, key_words=flat_key_words_list).setup_connector()
    interest_score_df = scraper.get_search_interest_score()
    LOGGER.info('pulled search interest scores.')

    LocalDriver(arguments=arguments).write(material_to_write=interest_score_df)
    LOGGER.info('results written on local machine.')

    return 0


if __name__ == "__main__":
    run_and_exit(InputArguments, main, description=__doc__, version="0.1.0")
