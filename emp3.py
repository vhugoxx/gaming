from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 2996268
api_hash = 'af5c9894512ba0234919e240764b13bd'
phone_number = '00351939426865'

client = TelegramClient('APISession_CFG_TT', api_id, api_hash)
client.start()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

my_private_channel_id = None
my_private_channel = None

for dialog in client.iter_dialogs():
    my_private_channel = dialog
    my_private_channel_id = dialog.id
    print(my_private_channel, my_private_channel_id)

