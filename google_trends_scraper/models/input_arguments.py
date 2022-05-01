from pydantic import BaseModel, Field, validator, root_validator
from pydantic_cli.examples import ExampleConfigDefaults
from pydantic_cli import HAS_AUTOCOMPLETE_SUPPORT


class InputArguments(BaseModel):
    class Config(ExampleConfigDefaults):
        CLI_SHELL_COMPLETION_ENABLE = HAS_AUTOCOMPLETE_SUPPORT

    source_input_location: str = Field(
        ...,
        title="Input CSV file full path.",
        description="Full path to the input csv file, including file name, which holds search key-words.",
        required=True,
        cli=("-i", "--input-path")
    )

    source_output_location: str = Field(
        ...,
        title="Output directory full path.",
        description="Full path to the local machine dir, to write results.",
        required=True,
        cli=("-o", "--output-path")
    )

    host_language: str = Field(
        'en-US',
        title="Language",
        description="Host language for accessing Google Trends.",
        required=True,
        cli=("-l", "--host-language")
    )

    time_zone: int = Field(
        360,
        title="Time zone.",
        description="Timezone offset.",
        required=True,
        cli=("-t", "--time-zone")
    )

    start_year: int = Field(
        ...,
        title="Start year for key words search.",
        description="Start year.",
        required=True,
        le=2022,
        cli=("-sy", "--start-year")
    )

    end_year: int = Field(
        ...,
        title="End year for key words search.",
        description="End year.",
        required=True,
        le=2022,
        cli=("-ey", "--end-year")
    )

    start_month: int = Field(
        ...,
        title="Start month for key words search.",
        description="Start month.",
        required=True,
        ge=1,
        le=12,
        cli=("-sm", "--start-month")
    )

    end_month: int = Field(
        ...,
        title="End month for key words search.",
        description="End month.",
        required=True,
        ge=1,
        le=12,
        cli=("-em", "--end-month")
    )

    start_day: int = Field(
        ...,
        title="Start day for key words search.",
        description="Start day.",
        required=True,
        ge=1,
        le=31,
        cli=("-sd", "--start-day")
    )

    end_day: int = Field(
        ...,
        title="End day for key words search.",
        description="End day.",
        required=True,
        ge=1,
        le=31,
        cli=("-ed", "--end-day")
    )

    start_hour: int = Field(
        ...,
        title="Start hour for key words search.",
        description="Start hour.",
        required=True,
        ge=0,
        le=24,
        cli=("-sh", "--start-hour")
    )

    # @validator('source_input_location')
    # check the existence of the file
    # def file_existence(cls, value):

    # @validator('source_input_location')
    # check the extension of the file
    # def file_extension(cls, value):
