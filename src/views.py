import json
from datetime import datetime


def date_time_to_json(date_time_str):
    try:
        date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        response = {
            "date": date_time_obj.date().isoformat(),
            "time": date_time_obj.time().isoformat(),
        }
    except ValueError:
        response = {"status": "error", "message": "Неверный формат даты и времени"}
    return json.dumps(response)


date_time_input = "2023-10-05 14:30:00"
json_output = date_time_to_json(date_time_input)
print(json_output)


Mw!@nWC2pBm9gD5