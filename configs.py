# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "7515868"))
    API_HASH = getenv("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")
    BOT_TOKEN = getenv("BOT_TOKEN", "7619312091:AAF47pVl0SYnVGW2aqYT8uVUEiQJ2uJan7g")
    FSUB = getenv("FSUB", "Telugu_Movies_999")
    CHID = int(getenv("CHID", "-1001798300759"))
    SUDO = list(map(int, getenv("SUDO", "6081617163").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://animefrnd44:OEgLPjMjrAKR46kE@cluster0.arcfjym.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
