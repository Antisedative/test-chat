import time
from datetime import datetime
from flask import Flask, request, render_template, json

app = Flask(__name__)


@app.route("/")
def index_page():
    return "HELLO"


db_file = "./data/db.json"
json_db = open(db_file, "rb")
data = json.load(json_db)
db = data["messages"]


def saveMessages():
    data = {
        "messages": db
    }
    json_db = open(db_file, "w")
    json.dump(data, json_db)


@app.route("/form")
def form():
    return render_template("form.html")


# POST - как правило означает изменение данных
# GET - запрос, который ничего не меняет

@app.route("/sendMessage")
def chat():
    name = request.args["name"]
    text = request.args["text"]

    name_len = len(name)  # длина имени
    text_len = len(text)  # длина текста

    if name_len > 100 or name_len < 3:
        return "ERROR"

    if text_len < 1 or text_len > 3000:
        return "ERROR"

    message = {
        "name": name,
        "text": text,
        "time": time.time()  # таймстемп
    }
    db.append(message)  # Добавляем новое сообщение в список\
    saveMessages()

    return "OK!"


def print_messages(messages):
    for message in messages:
        name = message["name"]
        text = message["text"]
        message_time = message["time"]
        time_pretty = datetime.fromtimestamp(message_time)
        print(f"[{name}] / {time_pretty}")
        print(text)
        print()


# http://127.0.0.1:5000/messages?after_timestamp=19191
# СОбирать все сообщения, после определенного времени
@app.route("/messages")
def get_messages():
    after_timestamp = float(request.args["after_timestamp"])
    result = []  # Все сообщения, отправленные после after_timestamp
    for message in db:
        if message["time"] > after_timestamp:
            result.append(message)

    return {"messages": result}


# print_messages(get_messages(time22_10))

app.run()
