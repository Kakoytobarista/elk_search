from pydantic_settings import BaseSettings


class ConfigELK(BaseSettings):
    index_name: str
    hosts: str
