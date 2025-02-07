import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize chatbot
chatbot = ChatBot(
    "Chatbot for Basic Customer support",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

# Huấn luyện chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Check bot trainer with corpus englist. We may not need it
try:
    trainer.train("chatterbot.corpus.english")
except Exception as e:
    print("Bot had training or error:", e)

# Get all data in traning data folder
training_folder = "training/data"
training_files = [
    os.path.join(training_folder, f) for f in os.listdir(training_folder) 
    if f.endswith(".yml")
]

# Checking yml files & training
if training_files:
    print(f"Traning {len(training_files)} file .yml...")
    trainer.train(*training_files)
    print("Chatbot had been training!")
else:
    print("Don't have any file .yml to training!")
