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

# Get all data in traning data folder
training_folder = "training/data"
training_files = [
    os.path.join(training_folder, f) for f in os.listdir(training_folder) 
    if f.endswith(".yml")
]

# Checking yml files
if training_files:
    print(f"Traning {len(training_files)} file .yml...")
    trainer.train(*training_files)
    print("Chatbot had been training!")
else:
    print("Don't have any file .yml to training!")
