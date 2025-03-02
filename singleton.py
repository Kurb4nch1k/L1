import json
import threading

class ConfigCache:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, config_file='config.json'):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ConfigCache, cls).__new__(cls)
                    cls._instance._load_config(config_file)
        return cls._instance

    def _load_config(self, config_file):
        with open(config_file, 'r') as file:
            self._config_data = json.load(file)

    def get(self, key):
        return self._config_data.get(key)

    def set(self, key, value):
        self._config_data[key] = value
        self._save_config()

    def _save_config(self):
        with open('config.json', 'w') as file:
            json.dump(self._config_data, file, indent=4)


if __name__ == "__main__":
    cache1 = ConfigCache()
    cache2 = ConfigCache()

    print(cache1.get("some_key"))  # Получение значения по ключу
    cache1.set("some_key", "new_value")  # Изменение значения
    print(cache2.get("some_key"))  # Проверка изменений через другой экземпляр