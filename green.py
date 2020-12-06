from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 2241619
api_hash = '71718cf1b0182ccd6bbca48e418c8343'
phone_number = '00351939426865'

client = TelegramClient('APISession_hugo', api_id, api_hash)
client.start()

print(client.get_me().stringify())

client.send_message('+351939426865', 'teste de python')

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

channel_username='https://t.me/joinchat/AAAAAFFVzbofUqSnF98mFQ' # your channel
channel_entity=client.get_entity(channel_username)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=2,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))
# messages stored in `posts.messages`

print('Channel Entity:', channel_entity)
print('Posts received:', posts)