# db.py
from pymongo import MongoClient
import os

# Use environment variable if present
MONGO_URI = os.getenv("MONGO_URI", "your-mongodb-connection-string")
client = MongoClient(MONGO_URI)
db = client["blogpilot"]
users_collection = db["users"]
