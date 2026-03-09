from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS").split(",")))
WEBAPP_URL = os.getenv("WEBAPP_URL")
DB_NAME = os.getenv("DB_NAME")
REFERRAL_BONUS = int(os.getenv("REFERRAL_BONUS"))
DAILY_BONUS_MIN = float(os.getenv("DAILY_BONUS_MIN"))
DAILY_BONUS_MAX = float(os.getenv("DAILY_BONUS_MAX"))
UNSUBSCRIBE_PENALTY_MULTIPLIER = int(os.getenv("UNSUBSCRIBE_PENALTY_MULTIPLIER"))
UNSUBSCRIBE_CHECK_HOURS = int(os.getenv("UNSUBSCRIBE_CHECK_HOURS"))
ADSGRAM_API_KEY = os.getenv("ADSGRAM_API_KEY")
ADS_REWARD = int(os.getenv("ADS_REWARD"))
GAME_777_MIN_BET = int(os.getenv("GAME_777_MIN_BET"))
GAME_777_MAX_BET = int(os.getenv("GAME_777_MAX_BET"))
LOG_LEVEL = os.getenv("LOG_LEVEL")