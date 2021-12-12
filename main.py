from pyrogram import Client
from pyrogram.raw import functions
import plyer
import keyboard
import time
import json
from datetime import datetime

config = json.loads(open('config.json').read())

with Client("app", config['API_ID'], config['API_HASH']) as app:
    def ChangeNick(nick):
        print('CHANGE NICK TO:', nick)
        app.send(functions.account.UpdateProfile(first_name=nick))
        plyer.notification.notify(message=f'Ник изменен на {nick}', title='Change Telegram Name')

    for key, value in config['NAMES'].items():
        keyboard.add_hotkey(key, ChangeNick, args=(value, ))
    
    ctime = ''
    while 1:
        now = datetime.now()
        now = datetime.strptime(f'{now.hour}:{now.minute}', '%H:%M')
        for key in list(config['TIME'].keys())[::-1]:
            d = datetime.strptime(key, '%H:%M')
            if now >= d:
                if ctime != config['TIME'][key]:
                    ChangeNick(config['TIME'][key])
                ctime = config['TIME'][key]
                break
        time.sleep(1)
