import json
import re


def filter_transactions_with_phone_numbers(transactions):
    phone_pattern = re.compile(
        r"(?:(?:\+7|8)\s?)?(?:\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{2}[\s-]?\d{2}"
    )
    filtered_transactions = [
        transaction
        for transaction in transactions
        if "description" in transaction
        and phone_pattern.search(transaction["description"])
    ]
    return json.dumps(filtered_transactions, ensure_ascii=False)



def filter_transactions_to_individuals(transactions):
    name_pattern = re.compile(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.$')

    filtered_transactions = [
    transaction for transaction in transactions
    if (transaction.get('category') == 'Переводы' and
    'description' in transaction and
     name_pattern.search(transaction['description']))
]

    return json.dumps(filtered_transactions, ensure_ascii=False)