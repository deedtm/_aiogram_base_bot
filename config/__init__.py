from configparser import ConfigParser

_config = ConfigParser()
_config.read('config.ini')

token = _config.get('telegram', 'token')
parse_mode = _config.get("telegram", "parse_mode")
disable_link_preview = _config.getboolean("telegram", "disable_link_preview")
