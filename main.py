from telethon import TelegramClient, events
from telethon.tl.custom.message import Message

### config information

# you can Replace Your Api-ID And Api-Hash From my.Telegram.org
api_id = 29793455
api_hash= "b5da6c4d2b72ee566b2451fcb91e4ee2"
client = TelegramClient('ForwardBot', api_id, api_hash,)


# Replace the group/user ID you want messages forwarded to.
Group_id = int(input("Insert GROUP ID (with -) Or USER ID you want the messages to be sent to:"))

### config information


@client.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))

async def forward_messages(event : Message):

   dataUser = await event.get_sender()

   fist_name = dataUser.first_name
   username = f"sender name:` {fist_name}` \nsender id: [{dataUser.id}](tg://user?id={dataUser.id})"

   # if event is have Self-Destructing Messages
   if event.message.media and hasattr(event.message.media, 'ttl_seconds') :

      sDM = getattr(event.message.media, 'ttl_seconds', None)

      if sDM!=None:
         MediaSDM = await event.download_media()

         await client.send_file(entity=Group_id, caption=username, file=MediaSDM, parse_mode="Markdown") #send media without type

      else:
         msg: Message = await client.forward_messages(entity=Group_id, messages=event.message)

         await client.send_message(entity=Group_id, message=username, reply_to=msg, parse_mode="Markdown")


   else:
      msg : Message = await client.forward_messages(entity=Group_id, messages=event.message)
      await client.send_message(entity=Group_id, message=username ,reply_to=msg, parse_mode="Markdown")



if __name__ == '__main__':
   client.start()
   if client.is_connected():
      print("self bot is connected.")
   client.run_until_disconnected()
