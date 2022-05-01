from pydantic import BaseModel, Field, validator, root_validator
from pydantic_cli.examples import ExampleConfigDefaults
from pydantic_cli import HAS_AUTOCOMPLETE_SUPPORT


class InputArguments(BaseModel):
    class Config(ExampleConfigDefaults):
        CLI_SHELL_COMPLETION_ENABLE = HAS_AUTOCOMPLETE_SUPPORT

    source_input_location: str = Field(
        ...,
        title="Input File",
        description="Path to the input file, which holds search key-words.",
        required=True,
        cli=("-i", "--input-location"),
    )
    source_output_location: str = Field(
        ...,
        title="Local path",
        description="Local machine path to write results.",
        required=True,
        cli=("-o", "--output-location"),
    )

    # @validator('source_input_location')
    # check the existence of the file
    # def file_existence(cls, value):

    # @validator('source_input_location')
    # check the extension of the file
    # def file_extension(cls, value):
