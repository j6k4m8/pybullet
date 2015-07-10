# pybullet
Use pushbullet from the command line. Featuring `sms [contact] [message]`

Currently a work in progress &mdash; contributions welcome!

# Setup
Clone this repo and rename the settings-file. Install requirements.
```
git clone git@github.com:j6k4m8/pybullet.git pybullet
cd pybullet
mv demo-settings.py settings.py
pip install requirements
```
Now edit `settings.py` with your own account data. Your account access token is [here](https://www.pushbullet.com/#settings/account). Device identifiers can be found by navigating to [the Pushbullet devices page](https://www.pushbullet.com/#devices) and clicking on your phone: The url of that page is then:
```
https://www.pushbullet.com/#devices/XXXXXzzzzzzzzzzz
```
The `XXXXX` is your `user_iden`, the full `X` and `z` string is your `device_iden`.

# Usage

| Command | Description |
|---------|-------------|
| <kbd>sms 2015555555 "hi there!"</kbd> | Send a message to a phone number |
| <kbd>contacts add jordan 9739039945</kbd> | Create a new contact |
| <kbd>sms jordan "you're a nerd!"</kbd> | Send a message to a contact |
| <kbd>sms jordan and you look goofy too</kbd> | No quotes needed! |
| <kbd>sms jordan \`ls\` | Send a contact the output of a bash script! Useful! |
| <kbd>contacts ls</kbd> | Also `contacts list` or `contacts l`: List contacts |
| <kbd>contacts ls jor</kbd> | Lists all contacts that contain the string `jor` |

In another shell (I use `tmux`), run <kbd>python ./stream.py</kbd>. This will open your Pushbullet stream and print the contact name (red) and their message (blue). *(Currently working on how to make this an interactive shell.)*


`contacts add` adds a line to a file called `.contacts`. The contents are hand-editable: Simply add a name, a tab (`\t`) and a phonenumber. No spaces in the number. If you get a `no such file` error when running `contacts` for the first time, simply <kbd>touch .contacts</kbd> and you're good to go.

# Contributing
Pull-requests welcome! Bug reports (via [the Issues page](https://github.com/j6k4m8/pybullet/issues)) also welcome.
