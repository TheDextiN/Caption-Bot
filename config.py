import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7253119834:AAFKqchLMFUVqGVQowGugwNqXkLuylaEAG0")
      API_ID = int(os.environ.get("APP_ID", 20707655))
      API_HASH = os.environ.get("API_HASH", "e490b538a8edddec7367959ca407e7ad")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "@peppylinks")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AvishkarPatil")
