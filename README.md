# Instagram Follow Bot
##### (open to name suggestions)

## Features:
- Follow a list of users on Instagram
- Print which users couldn't be found
- Doesn't unfollow currently followed users

## Setup:
- Download/clone this repository and navigate into the correct folder in CMD/PowerShell/other terminal
- [Install and set up Python 3](https://www.python.org/downloads/), if not already installed
- Set up [geckodriver](https://github.com/mozilla/geckodriver/releases) and add installation location to your `PATH` environmental variable
- Put your username/email/phone and password in `login_info.txt`**on lines 1 and 2**, respectively
- Put the exact usernames you want to follow in `want_to_follow.txt`, with **each username on a separate line**
- Run `pip install -r requirements.txt`
- Run `py main.py` (switch `py` with whatever works for your installation)
- Manually follow users that couldn't be found 
- OR re-evaluate your behavior; why don't people feel comfortable giving you their real username?
