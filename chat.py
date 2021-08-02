import time
from datetime import datetime

time22_00 = datetime.fromisoformat("2021-08-02 22:00:00").timestamp()
time22_10 = datetime.fromisoformat("2021-08-02 22:10:00").timestamp()

test_message1 = {
  "text": "Hello, Ivan",
  "name": "Leonid",
  "time": time22_00
}

test_message2 = {
  "text": "How are you?",
  "name": "John",
  "time": time22_10
}
# key + value


# DataBase - база данных с сообщениями чата
# Список сообщений
db = [
  test_message1,
  test_message2
]

def chat(name,text):
  message = {
    "name": name,
    "text": text,
    "time": time.time() # таймстемп
  }
  db.append(message) # Добавляем новое сообщение в список

chat("Misha", "How did you walk yesterday?")
chat("Sasha", "How are you feeling?")

def print_messages(messages):
  for message in messages:
    name = message["name"]
    text = message["text"]
    message_time = message["time"]
    time_pretty = datetime.fromtimestamp(message_time)
    print(f"[{name}] / {time_pretty}")
    print(text)
    print()

# СОбирать все сообщения, после определенного времени
def get_messages(after_timestamp):
  result = [] #  Все сообщения, отправленные после after_timestamp
  for message in db: 
   if message["time"] > after_timestamp:
     result.append(message)
  
  return result

print_messages(get_messages(time22_10))