from pydantic_cli import run_and_exit

from google_trends_scraper.models.input_arguments import InputArguments

from google_trends_scraper.input_reader import InputReaderInterface
from google_trends_scraper.output_writer import LocalDriver

from google_trends_scraper.key_words_scraper import ScraperInterface


def main(arguments: InputArguments) -> int:
    """ Main interface entrypoint. """

    key_words = InputReaderInterface(input_source_location=arguments.source_input_location).read_csv().table.values
    flat_key_words_list = [item for sublist in key_words for item in sublist]

    scraper = ScraperInterface(arguments=arguments, key_words=flat_key_words_list).setup_connector()
    interest_score_df = scraper.get_search_interest_score()

    LocalDriver(arguments=arguments).write(material_to_write=interest_score_df)

    return 0


if __name__ == "__main__":
    run_and_exit(InputArguments, main, description=__doc__, version="0.1.0")
