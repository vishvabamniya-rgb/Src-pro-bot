# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "29587646"))
API_HASH = getenv("API_HASH", "4240637ac356f0c7cb02a293264304d1")
BOT_TOKEN = getenv("BOT_TOKEN", "8264377091:AAFw9MDFqZsrHRpPR7qug348KLc-ugzJCb0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8348589128").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003086729312")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002656585987"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
