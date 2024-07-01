import json
from typing import Any, Dict


class ConfigStore:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def get(self, key: str) -> Any:
        return self.config[key]

    def set(self, key: str, value: Any):
        self.config[key] = value

    def get_all(self) -> Dict[str, Any]:
        return self.config

    def set_all(self, config: Dict[str, Any]):
        self.config = config

    def save(self, path: str):
        with open(path, "w") as f:
            json.dump(self.config, f, indent=4)

    @staticmethod
    def load(path: str) -> "ConfigStore":
        with open(path, "r") as f:
            return ConfigStore(json.load(f))

    def __str__(self):
        return json.dumps(self.config, indent=4)
    


config_store = ConfigStore({})

def setConfig(key: str, value: Any):
    config_store.set(key, value)

def getConfig(key: str) -> Any:
    return config_store.get(key)