from telethon import TelegramClient
import datetime, re, sys, os
import requests

api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
client = TelegramClient('/home/abhi/docker/config/code-server/workspace/tg/telethon/anon', api_id, api_hash)
date = datetime.date.today()

dict = {}

async def main():
    async for message in client.iter_messages(-760973741, offset_date=date, reverse=True):
        x = re.findall(r"\d+", message.text)
        bill = int(x[0])
        amt = int(x[1])
        dict[bill]=amt

with client:
    client.loop.run_until_complete(main())
    text = f"{datetime.date.today():%A - %d %B %Y}\n\n{len(dict)} Bills For ₹{sum(dict.values())}\n\nAverage - ₹{round(sum(dict.values())/len(dict.values()))}/bill"
    requests.post(f"{os.environ['IP']}/smc", data=text.encode('utf-8'), headers={"content-type": "text/plain"})
    sys.stdout.flush()