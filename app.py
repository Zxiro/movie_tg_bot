from flask import Flask, request
from telegram import Bot
from secrets import telegram_bot_token

app = Flask(__name__)
bot = Bot(telegram_bot_token)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    # Process the update using your bot logic
    bot.process_update(update)
    return 'OK', 200

@app.route('/', methods=['POST'])
def post():
    if request.method == 'POST':
        # Access POST data from the request
        msg = request.get_json() 

        print(msg)

        return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
