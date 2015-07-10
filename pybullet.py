from settings import *
import urllib
import urllib2
import requests
import json


def push_sms(number, message):
    url = 'https://api.pushbullet.com/v2/ephemerals'
    values = {
        "type": "push",
        "push": {
            "type": "messaging_extension_reply",
            "package_name": "com.pushbullet.android",
            "source_user_iden": settings["PUSHBULLET_USER_IDEN"],
            "target_device_iden": settings["PUSHBULLET_SMS_IDEN"],
            "conversation_iden": number,
            "message": message
        }
    }

    headers = {"Authorization" : "Bearer " + settings["PUSHBULLET_API_KEY"]}

    res = requests.post(url, data=json.dumps(values), headers=headers)


def push_string(message):
    url = 'https://api.pushbullet.com/v2/ephemerals'
    values = {
        "type": "push",
        "push": {
            "type":"clip",
            "body":"http://www.google.com",
            "source_user_iden": str(settings["PUSHBULLET_USER_IDEN"]),
        }
    }

    headers = {"Authorization" : "Bearer " + str(settings["PUSHBULLET_API_KEY"])}

    data = urllib.urlencode(values)
    print data
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    return response

