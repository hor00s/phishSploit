
![Logo](https://i.imgur.com/wT7hSNC.png)


# ~ phishSploit ~

A tool to create a a clone of a social-media
platform and share either locally or even on-line
with a few key-strokes!


## Authors

- [@hor00s](https://www.github.com/hor00s)


## Contributing

Contributions are always welcome!




## FAQ

#### What purpose is this service?

Nothing but only you can protect your self from
a phising attack. What is a better way to protect
your self other that actually knowing what 
social [engineer](https://www.imperva.com/learn/application-security/social-engineering-attack/)/[phising](https://www.imperva.com/learn/application-security/phishing-attack-scam/)
attack is and how it works?

#### Isnt't this illegal?

Well, yes and no. As long as the application is
used with consent and explicit permission it's not!


#### Will my sites stay online for ever?

No, all the services that are used so far have a
limit per session so expect your sites to go down
after a couple of hours at most!

## Documentation

**~ Make sure you've seen the DISCLAIMER.md ~**

phishSploit is an application that creates clone
login pages from well known social media platforms.
These pages have some ways of sharing easily either
locally or publicly with the following options:
- private: Opens at `127.0.0.1:<PORT>` and stays only on the host machine
- local: Opens at `<your-IPv4-addr>:<PORT>` and can be shared to all the devices that are connected on the same netword
- ngrok: Opens at a random link every time given from [ngrok](https://ngrok.com/docs)'s tunneling service and can be accessed from anywhere arround the world
- localtunnel: Opens at a random link every time given from [localtunnel](https://theboroer.github.io/localtunnel-www/)'s tunneling service and can be accessed from anywhere arround the world

The app will then prompt you to add a `redirect url`. This url is where a victim will be redirected after he inserts his credentials. If this field is left blank, the default of each page (Chosen page's homepage) will be set by default

Your page clone can be shared publicly with [pinggy.io](https://pinggy.io/) too.
```
Start the app on private mode (Option [2])
Open a new terminal
$ ssh -p 443 -R0:127.0.0.1:<PORT> a.pinggy.io
#              ^ That's a Zero (0)
Share the link
```

Note that none of these services provides anonimity
and/or confidentiality, so use wisely!

The application also has a cli. Run `./phish_sploit.py -h` for more info.

## Installation

- Basic Installation

```bash
  git clone https://github.com/hor00s/phishSploit
  cd phishSploit/code
  pip install -r requirements.txt
  python3 phish_sploit.py
  # That should be enought for most of the services to work
```

- Ngrok service does not work out of the box. To install:

```
  Create an account to ngrok: https://ngrok.com/
  Get your auth-token
  Download the app: https://ngrok.com/download
  Navigate to the same directory that the `ngrok.exe` is downloaded
  Open terminal
  $ ngrok config add-authtoken <TOKEN>
```

## ~ Keep it fun, safe and legal!
