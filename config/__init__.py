from configparser import ConfigParser

_config = ConfigParser()
_config.read('config.ini')

token = _config.get('telegram', 'token')
