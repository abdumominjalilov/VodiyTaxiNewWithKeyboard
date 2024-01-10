# from pymongo import MongoClient
# client = MongoClient(
#     "mongodb+srv://Abdul_Mumin:abdumominjalilov8@cluster0.bk3khgw.mongodb.net/Telegram_bot?retryWrites=true&w=majority")
import motor.motor_asyncio
from pymongo.server_api import ServerApi

url = "mongodb+srv://Abdul_Mumin:abdumominjalilov8@cluster0.bk3khgw.mongodb.net/Telegram_bot?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(url, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("MongoDb ga Ulandi")
except Exception as e:
    print(e)
# db = client.Telegram_bot.Telegram
db = client["Telegram"]
collectionCs = db["customers"]
collectionDr = db["drivers"]
collectionAll = db["users"]
products = db["products"]
collectionEnd_Dr = db["Telegram_End"]
collectionEnd_Cs = db["Telegram_EndCs"]


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://Abdul_Mumin:<password>@cluster0.bk3khgw.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
