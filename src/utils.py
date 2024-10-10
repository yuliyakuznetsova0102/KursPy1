import json
from datetime import datetime, time


def greetings_time():
    now = datetime.now()
    current_time = now.time()
    if current_time <= time(hour=12):
        greeting = "Доброе утро"
    elif current_time <= time(hour=18):
        greeting = "Добрый день"
    else:
        greeting = "Добрый вечер"
    response = {"greeting": greeting}
    return json.dumps(response, ensure_ascii=False)

print(greetings_time())



