from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Check and exist sqlite
english_bot = ChatBot(
    "Chatbot for Basic Customer support",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm sorry, I didn't understand. Can you rephrase?",
            "maximum_similarity_threshold": 0.7
        }
    ]
)

# Check bot trainer with corpus englist. We may not need it
trainer = ChatterBotCorpusTrainer(english_bot)
try:
    trainer.train("chatterbot.corpus.english")
except Exception as e:
    print("Bot had training or error:", e)

@app.route("/chat", methods=["POST"])
def get_bot_response():
    data = request.get_json()
    user_text = data.get("message")

    if not user_text:
        return jsonify({"error": "Message is required"}), 400

    response = str(english_bot.get_response(user_text))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
