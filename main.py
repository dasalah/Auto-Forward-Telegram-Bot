from telethon import TelegramClient, events
from telethon.tl.custom.message import Message


### config information

# Replace Your Api-ID And Api-Hash From my.Telegram.org
api_id= 7960798
api_hash="481fb8835f23b673264c49abfc092122"
# Replace the group ID you want messages forwarded to.
Group_id = -1002333182557

### config information


client = TelegramClient('ForwardBot', api_id, api_hash)


@client.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))

async def forward_messages(event : Message):

   DataUser = await event.get_sender()

   fist_name = DataUser.first_name
   last_name = DataUser.last_name if DataUser.last_name else '' #don't show last name and return None
   username = f"sender name:` {fist_name} {last_name} ` \nsender id: [{DataUser.id}](tg://user?id={DataUser.id})"


   if event.message.media and hasattr(event.message.media, 'ttl_seconds') :#if event is have Self-Destructing Messages

      SDM = getattr(event.message.media , 'ttl_seconds',None)

      if SDM!=None:
         MediaSDM = await event.download_media(file = bytes)

         await client.send_file(entity=Group_id, caption=username, file=MediaSDM, parse_mode="Markdown") #send media without type

      else:
         msg: Message = await client.forward_messages(entity=Group_id, messages=event.message)

         await client.send_message(entity=Group_id, message=username, reply_to=msg, parse_mode="Markdown")


   else:
      msg : Message = await client.forward_messages(entity=Group_id, messages=event.message)

      await client.send_message(entity=Group_id, message=username ,reply_to=msg, parse_mode="Markdown")



if __name__ == '__main__':
   client.start()
   client.run_until_disconnected()
