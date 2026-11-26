import os
import yaml
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Settings:

    def __init__(self):

        env = os.getenv(
            "ENVIRONMENT",
            "dev"
        )

        config_path = (
            Path("configs")
            / f"{env}.yaml"
        )

        with open(config_path) as file:

            self.config = yaml.safe_load(file)


    @property
    def environment(self):

        return self.config["environment"]


    @property
    def database(self):

        return self.config["database"]


    @property
    def aws(self):

        return self.config["aws"]



settings = Settings()