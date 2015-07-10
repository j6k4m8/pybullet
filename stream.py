import websocket
import thread
import time
import messenger
from settings import *
import logging
import json
logging.basicConfig()


def on_message(ws, message):
    message = json.loads(message)
    if message['type'] == 'push' and 'title' in message['push'] and 'body' in message['push']:
        messenger.add_message(message['push']['title'], message['push']['body'])
    # messenger.loop_get_response()

def on_error(ws, error):
    print error

def on_close(ws):
    print "Stream closed."

def on_open(ws):
    pass


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://stream.pushbullet.com/websocket/" + settings["PUSHBULLET_API_KEY"],
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
