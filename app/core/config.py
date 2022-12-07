import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "TroVol Backend"
    title: str = "TroVol example application"
    api_prefix: str = "/trovol-backend"
    debug: bool = True

    class Config:
        env_file = ".venv/my-env/"


class DevSettings(Settings):
    region_name = 'ap-southeast-1'
    dynamo_link = 'devdynamo'
    buckets = 'trovol'
    table = 'TroVol-Stagting1'
    # table = 'TroVol'


class StagingSettings(Settings):
    region_name = 'ap-southeast-1'
    dynamo_link = 'stagingdynamo'
    buckets = 'trovol'
    table = 'TroVol-Stagting1'


def get_settings():
    env = os.environ.get('env')
    if env == 'dev':
        return DevSettings()
    elif env == 'staging':
        return StagingSettings()
    return DevSettings()


config = get_settings()
print(os.environ.get('env'))
