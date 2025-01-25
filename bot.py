# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Create sessions directory with proper permissions
sessions_dir = "sessions"
if not os.path.exists(sessions_dir):
    os.makedirs(sessions_dir, mode=0o777)

class Bot(Client):

    def __init__(self):
        super().__init__(
            f"{sessions_dir}/techvj_login",  # Modified session path
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10,
            workdir=os.getcwd()  # Explicitly set working directory
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
