import os
import datetime as dt
from colorama import Fore


TODAY:     str      = dt.datetime.now().strftime("%Y-%m-%d")
ERRORTXT:  str      = os.path.join('..', 'error_log.txt')
BANNER:    str      = os.path.join('..', 'banner.txt')
URL:       str      = os.path.join('..', 'url.txt')
LOGSTXT:   str      = os.path.join('..', 'logs')
PUBLICURL: str      = None
LOAD_STEP: float    = 12.5
LOAD_TIME: float    = 8.0


PVT_TUNNELS: tuple = (
    'private',
    'local',
)

PUBLIC_TUNELS: tuple = (
    'ngrok',
    'localtunnel',
)


def success(msg: str) -> str:
    return f"{Fore.GREEN}[SUCCESS]: {msg}"


def info(msg: str) -> str:
    return f"{Fore.YELLOW}[INFO]: {msg}"


def warning(msg: str) -> str:
    return f"{Fore.RED}[WARNING]: {msg}"


def theme_color(banner: str) -> str:
    return f"{Fore.LIGHTCYAN_EX}{banner}"
