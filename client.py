from telethon import TelegramClient, events, sync

# https://core.telegram.org/api/obtaining_api_id
api_id = 1234567
api_hash = '#########'

client = TelegramClient('session_name', api_id, api_hash)
async def main():
    
    me = await client.get_me()
    print(me.username)
    print(me.phone)

    chat_id = -1
    
    async for dialog in client.iter_dialogs():
        if "CHAT_NAME" in dialog.name:
            print(dialog.name, 'has ID:', dialog.id)
            chat_id = dialog.id

    
    await client.send_message(chat_id, 'Downloding')
    
    f = open("output.txt", "a")
    
    async for message in client.iter_messages(chat_id):
        text = message.text
        if text is not None:
            if "music.yandex" in text:
                f.write(text + '\n')
                print(message.id)

    await client.send_message(chat_id, 'Finished!')

    f.close()

with client:
    client.loop.run_until_complete(main())
