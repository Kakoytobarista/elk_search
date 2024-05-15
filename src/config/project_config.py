import os

import yaml
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

from config.elk.elk_config import ConfigELK

load_dotenv()

def get_conf_path():
    conf_filename = 'config/config_test.yaml'
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    grandparent_dir = os.path.dirname(parent_dir)
    path = os.path.join(grandparent_dir, conf_filename)
    return os.getenv("CONF_PATH", path)

class AppConfig(BaseSettings):
    service_name: str = "search_app"
    elk: ConfigELK
    debug: bool = True
    version: str = '1.0.0'

    @classmethod
    def from_yaml_file_sync(cls, config_path: str) -> "AppConfig":
        with open(config_path, mode="r") as f:
            contents = f.read()
            return cls.model_validate(yaml.full_load(contents))


app_config = AppConfig.from_yaml_file_sync(get_conf_path())
