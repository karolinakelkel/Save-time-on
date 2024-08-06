import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Loads configuration parameters from environment variables.

    Class Attributes:
    FIREBASE_DB_CONFIG_PATH (str): The path to the Firebase database configuration file.
    FIREBASE_DB_URL (str): The URL for accessing the Firebase database.
    OPENAI_API_KEY (str): The API key for accessing OpenAI.
    """

    FIREBASE_DB_CONFIG_PATH = os.getenv('FIREBASE_DB_CONFIG_PATH')
    FIREBASE_DB_URL = os.getenv('FIREBASE_DB_URL')

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    @staticmethod
    def validate_environment_variables():
        """
        Validates that all necessary environment variables are set.

        :raises ValueError: If any of the required environment variables are not set.
        """

        if not Config.FIREBASE_DB_CONFIG_PATH:
            raise ValueError('Database configuration file path (FIREBASE_DB_CONFIG_PATH) is not set in environment '
                             'variables')
        if not Config.FIREBASE_DB_URL:
            raise ValueError('Database URL (FIREBASE_DB_URL) is not set in environment variables')
        if not Config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key (OPENAI_API_KEY) is not set in environment variables")
