from settings import *
import urllib
import urllib2


def pushSms(number, message):
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

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    return response

pushSms('9739039945', 'HI!')
