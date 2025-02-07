from flask import Flask, request, jsonify, Blueprint
from chatterbot import ChatBot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Check and exist sqlite
chatbot = ChatBot(
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

# Create a blueprint for version 1 of the API
v1 = Blueprint("v1", __name__, url_prefix="/api/v1")
CORS(v1)

@v1.route("/chat", methods=["POST"])
def get_bot_response():
    data = request.get_json()
    user_text = data.get("message")

    if not user_text:
        return jsonify({"error": "Message is required"}), 400

    response = str(chatbot.get_response(user_text))
    return jsonify({"response": response})

app.register_blueprint(v1)
if __name__ == "__main__":
    app.run(debug=True)
