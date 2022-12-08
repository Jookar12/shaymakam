import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13930025"))
    API_HASH = os.environ.get("API_HASH", "3d5eb0aacd1eeadfd50feb229d2c6b7b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu20jvynpUF1mjr0BypT0v2yDhLuJXdwpMKLHZoz3MwXTQMp2N4kbhxhTsHhh4j8hF6XYV4AQyhML7mk8Lv8PBYdPrWu74JkuFXCh7aMzXsyit4Tkz1RfYj2nzCiqvPdZh4v2VgxKRvgkifLDHa5iu9UWhLw-7P6XKBaTsHA5cf8o7i-j-1N8krPebgoU7eugx4rOOF8vCVzcYZf9bMO9bryiqXMG4vVplFfBEssNGnJQHebLFQ8VNElKLEpD9nZ55i3lJMsWsVhHp11IkwwfoDVv2v8fz1CcIQt5OBTkQSnQDjwSnIg-zvLpOnWGuOSRPZWX-ByEnpj8r_yxyUPbSH8=") #Pastw string Sess
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/e9af719f1b5a3c5858243.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/ab880fc7a6737de3c7a7a.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', true) # Change it to "True" #optional
