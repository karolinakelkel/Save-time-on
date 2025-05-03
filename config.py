import os
from dotenv import load_dotenv


class Config:
    """
    Configuration loader and validator.

    Loads required environment variables using dotenv and validates their presence.
    """

    def __init__(self) -> None:
        load_dotenv()

        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.ffmpeg_path = os.getenv('FFMPEG_PATH')

        self._validate_environment_variables()

    def _validate_environment_variables(self) -> None:
        """
        Validates that all required environment variables are set.

        Raises:
            ValueError: If any of the required variables are missing.
        """

        missing_vars = []

        if not self.openai_api_key:
            missing_vars.append('OPENAI_API_KEY')
        if not self.ffmpeg_path:
            missing_vars.append('FFMPEG_PATH')

        if missing_vars:
            raise ValueError(f'Missing required environment variables: {', '.join(missing_vars)}')
