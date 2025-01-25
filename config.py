import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8179291116:AAGjClkWSlsOZtJLeo-fsLZFGXuoIJlzqAE")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "5625170"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "77633c2757f8697650e0c31cf505ffbc")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5723551431"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://himanshu12feb2k23:JaU8qjZ53Q8mWbP0@cluster0.keoec.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Database channel ID
DATABASE_CHANNEL = -1001631127601  # Replace with your channel ID
