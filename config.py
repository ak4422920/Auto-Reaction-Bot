from os import environ

API_HASH = environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
API_ID = int(environ.get("API_ID", "29171167"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_OWNER = int(environ.get("BOT_OWNER", "7251898668"))
BOT_USERNAME = environ.get("BOT_USERNAME", "Autoreactionakbot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002264638393"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002442422204"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://tg:tg@cluster0.fekvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
