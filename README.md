# pybullet
Use pushbullet from the command line. Featuring `sms 'contactname' 'message-to-send'`

Currently a work in progress -- trying to set things up!

# Setup
Rename demo-settings.py to `settings.py` and add your account data. I added the python scripts to my PATH so I can execute from anywhere. But duh that's optional.

# Usage
**Send a message to a phonenumber:**
```sms 2015555555 "hi there!"```

**Send a message to a contact:**
```sms jordan "you're a nerd!"```

**Add a new contact:**
```contacts add jordan 9739039945```

This adds a line to a file called `.contacts`. The contents are hand-editable: Simply add a name, a tab (`\t`) and a phonenumber. No spaces in the number.

# Contributing
Pull-requests welcome!
