import datetime as dt
from jsonwrapper import AutoSaveDict
from colorama import Fore
from pathlib import Path

ABSOLUTE_DIR = Path(__file__).parent.parent.parent

TODAY: str = dt.datetime.now().strftime("%Y-%m-%d")
ERRORTXT: str = Path(ABSOLUTE_DIR, 'error_log.txt')
BANNER: str = Path(ABSOLUTE_DIR, 'banner.txt')
URL: str = Path(ABSOLUTE_DIR, 'url.txt')
LOGSTXT: str = Path(ABSOLUTE_DIR, 'logs')
CONFIG_FILE: str = Path(ABSOLUTE_DIR, '.config.json')
PUBLICURL: str = None
LOAD_STEP: float = 12.5
LOAD_TIME: float = 8.0


PVT_TUNNELS: tuple = (
    'private',
    'local',
)

PUBLIC_TUNELS: tuple = (
    'ngrok',
    'localtunnel',
)

CONFIG = {
    'port': 5000,
}

config = AutoSaveDict(CONFIG_FILE, **CONFIG)
config.init()

def success(msg: str) -> str:
    return f"{Fore.GREEN}[SUCCESS]: {msg}"


def info(msg: str) -> str:
    return f"{Fore.YELLOW}[INFO]: {msg}"


def warning(msg: str) -> str:
    return f"{Fore.RED}[WARNING]: {msg}"


def theme_color(banner: str) -> str:
    return f"{Fore.LIGHTCYAN_EX}{banner}"
