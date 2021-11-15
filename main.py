from pyrogram import Client
from pyrogram.raw import functions
import plyer
import keyboard
import time

config = {
    'API_ID': 0000000,
    'API_HASH': 'XXXXXXXXXXXXXXXX',
    'NAMES': {
        'Ctrl + 1': 'RAYCON',
        'Ctrl + 2': 'RAYCON (sleep)',
        'Ctrl + 3': 'RAYCON (working)',
        'Ctrl + 4': 'RAYCON (game)'
    }
}

with Client("app", config['API_ID'], config['API_HASH']) as app:
    def ChangeNick(nick):
        app.send(functions.account.UpdateProfile(first_name=nick))
        plyer.notification.notify(message=f'Ник изменен на {nick}', title='Change Telegram Name')

    for key, value in config['NAMES'].items():
        keyboard.add_hotkey(key, ChangeNick, args=(value, ))
    while 1:
        time.sleep(1000)
