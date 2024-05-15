import sys

from pydantic_settings import BaseSettings

TEST_ENV = "--test-env" in sys.argv


class ConfigELK(BaseSettings):
    index_name: str
    hosts: str
