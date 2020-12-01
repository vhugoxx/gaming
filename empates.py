from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 2996268
api_hash = 'af5c9894512ba0234919e240764b13bd'

client = TelegramClient('APISession', api_id, api_hash)
client.start()

print(client.get_me().stringify())

client.send_message('+351939426865', 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo('me')

messages = client.get_messages('+351910825970')
print(messages)
# message
s[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')