

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")


# # Trial
bot = ChatBot('Career_Bot',storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(bot)
conv = open('Meet.txt','r').readlines()
trainer.train(conv)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
