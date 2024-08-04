from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """
    Loads configuration parameters from environment variables.

    Class Attributes:
    DB_NAME (str): The name of the database.
    DB_USER (str): The database user.
    DB_PASSWORD (str): The password for the database user.
    DB_HOST (str): The database host (default is 'localhost').
    DB_PORT (str): The database port (default is '5432').
    OPENAI_API_KEY (str): The API key for accessing OpenAI.
    """

    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD', None)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    @staticmethod
    def validate_environment_variables():
        """
        Validates that all necessary environment variables are set.

        :raises ValueError: If any of the required environment variables are not set.
        """

        if not Config.DB_NAME:
            raise ValueError('Database name (DB_NAME) is not set in environment variables')
        if not Config.DB_USER:
            raise ValueError('Database user (DB_USER) is not set in environment variables')
        if not Config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key (OPENAI_API_KEY) is not set in environment variables")


Config.validate_environment_variables()
