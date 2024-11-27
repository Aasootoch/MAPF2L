from os import environ as env
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Telegram:
    # Ensure that these environment variables are fetched correctly
    API_ID = int(env.get("API_ID", 22420478))  # Default to 22420478 if not set
    API_HASH = str(env.get("API_HASH", "5938b801d270c81afd3ad8581aba7960"))  # Default to the given value if not set
    BOT_TOKEN = str(env.get("BOT_TOKEN", "8117854408:AAEwP-_5q_Qi2Yu6e8ClA_OHfT_ftmjf3eo"))  # Default to the given value
    OWNER_ID = int(env.get('OWNER_ID', '7011650566'))  # Default to '7011650566' if OWNER_ID is not set
    WORKERS = int(env.get("WORKERS", "6"))  # Default to 6 if WORKERS is not set
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://ashu2626ranjan:9IxsVd6P2kIG6cEa@cluster0ddf566.0mtc8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0ddf566'))  # Default MongoDB URL
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', '1001807477865'))  # Default to @MAPOriginals if not set
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))  # Default to 'FileStream' if not set
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)  # Optional environment variable, can be None
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', '-1001807477865' 'True')  # Default to 'False' if not set
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False  # Convert to boolean
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))  # Default to 60 if not set
    FILE_PIC = env.get('FILE_PIC', "https://t.me/c/1815280589/259940")  # Default image URL
    START_PIC = env.get('START_PIC', "https://envs.sh/zmS.png")  # Default image URL
    VERIFY_PIC = env.get('VERIFY_PIC', "https://envs.sh/zmI.png")  # Default image URL
    MULTI_CLIENT = False  # Default is False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", -1002312973003))  # Default channel ID for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", -1002250712388))  # Default channel ID for user logs
    MODE = env.get("MODE", "primary")  # Default to 'primary' if MODE is not set
    SECONDARY = True if MODE.lower() == "secondary" else False  # Check if it's secondary mode
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))  # List of authorized users, default to OWNER_ID

class Server:
    # Using the provided server info, with updated port
    PORT = int(env.get("PORT", 9090))  # Default to 9090 if not set
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "galaxy.usbx.me"))  # Set the server hostname to 'galaxy.usbx.me'
    IP_ADDRESS = str(env.get("IP_ADDRESS", "46.232.210.217"))  # Set the IP address to '46.232.210.217'
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))  # Default to 1200 if not set
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")  # Convert to boolean
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")  # Convert to boolean
    FQDN = str(env.get("FQDN", BIND_ADDRESS))  # Use BIND_ADDRESS as fallback if FQDN is not set
    
    # Construct the URL for the server
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
