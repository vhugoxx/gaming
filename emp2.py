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

channel_username='@VitorVale' # your channel
channel_entity=client.get_entity(channel_username)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=100,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))
# messages stored in `posts.messages`

print('Channel Entity:', channel_entity)
print('Posts received:', posts)