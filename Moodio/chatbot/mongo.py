from pymongo import MongoClient
from django.conf import settings

from pymongo import MongoClient


# ✅ Get values from settings.py
MONGO_URI = getattr(settings, "MONGO_URI", None)
MONGO_DB_NAME = getattr(settings, "MONGO_DB_NAME", None)


client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
db = client[MONGO_DB_NAME]

users_col = db["users"]
chat_history_col = db["chat_history"]
quiz_results_col = db["quiz_results"]
roadmaps_col = db["roadmaps"]

# Test
print("✅ Connected to MongoDB:", db.list_collection_names())