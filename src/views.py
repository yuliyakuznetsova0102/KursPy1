import json
import pandas as pd
from datetime import datetime
import numpy

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





def get_excel(formatting):
    current_transactions = []
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        for transaction in get_excel_file.to_dict(orient="records"):
            transaction = {
                key: (
                    None if isinstance(value, float) and numpy.isnan(value) else value
                )
                for key, value in transaction.items()
            }
            current_transactions.append(transaction)
        return current_transactions
    else:
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")
