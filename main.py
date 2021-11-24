from pyrogram import Client
from pyrogram.raw import functions
import plyer
import keyboard
import time
import json

config = json.loads(open('config.json').read())

with Client("app", config['API_ID'], config['API_HASH']) as app:
    def ChangeNick(nick):
        app.send(functions.account.UpdateProfile(first_name=nick))
        plyer.notification.notify(message=f'Ник изменен на {nick}', title='Change Telegram Name')

    for key, value in config['NAMES'].items():
        keyboard.add_hotkey(key, ChangeNick, args=(value, ))
    while 1:
        time.sleep(1000)
