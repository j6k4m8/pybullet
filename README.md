# pybullet
Use pushbullet from the command line. Featuring `sms 'contactname' 'message-to-send'`

Currently a work in progress -- trying to set things up!

# Setup
Clone this repo and rename the settings-file.
```
git clone git@github.com:j6k4m8/pybullet.git pybullet
cd pybullet
mv demo-settings.py settings.py
```
Now edit `settings.py` with your own account data. Your account access token is [here](https://www.pushbullet.com/#settings/account). Device identifiers can be found by navigating to [the Pushbullet devices page](https://www.pushbullet.com/#devices) and clicking on your phone: The url of that page is then:
```
https://www.pushbullet.com/#devices/XXXXXzzzzzzzzzzz
```
The `XXXXX` is your `user_iden`, the full string is your `device_iden`.

# Usage
**Send a message to a phonenumber:**
```./sms 2015555555 "hi there!"```

**Send a message to a contact:**
```./sms jordan "you're a nerd!"```

**Add a new contact:**
```./contacts add jordan 9739039945```

**See your contacts:**
```./contacts list```

**See your contacts, with a filter (returns everything that contains your string):**
```./contacts list jo```

This adds a line to a file called `.contacts`. The contents are hand-editable: Simply add a name, a tab (`\t`) and a phonenumber. No spaces in the number. If you get a `no such file` error when running `contacts` for the first time, simply
```
touch .contacts
```
and you're good to go.

# Contributing
Pull-requests welcome!
