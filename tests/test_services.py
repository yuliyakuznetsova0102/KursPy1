import json

from src.services import filter_transactions_to_individuals, filter_transactions_with_phone_numbers


def test_filter_transactions_with_phone_numbers():
    transactions = [
        {"id": 1, "description": "Оплата +7 (123) 456-78-90"},
        {"id": 2, "description": "Без номера телефона"},
        {"id": 3, "description": "Звонок по номеру 8-987-654-32-10"},
        {"id": 4, "description": "Покупка на сайте"},
        {"id": 5, "description": "Контакт: 123 456 78 90"},
    ]
    expected_result = [
        {"id": 1, "description": "Оплата +7 (123) 456-78-90"},
        {"id": 3, "description": "Звонок по номеру 8-987-654-32-10"},
        {"id": 5, "description": "Контакт: 123 456 78 90"},
    ]

    result = filter_transactions_with_phone_numbers(transactions)
    assert json.loads(result) == expected_result


def test_filter_transactions_no_matches():
    transactions = [
        {"id": 1, "description": "Нет номера"},
        {"id": 2, "description": "Еще один без номера"},
    ]

    result = filter_transactions_with_phone_numbers(transactions)
    assert json.loads(result) == []


def test_filter_transactions_empty_list():
    transactions = []
    result = filter_transactions_with_phone_numbers(transactions)
    assert json.loads(result) == []


def test_filter_transactions_with_varied_phone_formats():
    transactions = [
        {"id": 1, "description": "Позвоните по номеру 8 123 456 78 90"},
        {"id": 2, "description": "Контакт: +7-987-654-32-10"},
    ]
    expected_result = [
        {"id": 1, "description": "Позвоните по номеру 8 123 456 78 90"},
        {"id": 2, "description": "Контакт: +7-987-654-32-10"},
    ]
    result = filter_transactions_with_phone_numbers(transactions)
    assert json.loads(result) == expected_result


def test_filter_transactions_to_individuals():
    transactions = [
        {"id": 1, "category": "Переводы", "description": "Иванов И."},
        {"id": 2, "category": "Покупки", "description": "Товар"},
        {"id": 3, "category": "Переводы", "description": "Петров П."},
        {"id": 4, "category": "Переводы", "description": "Некорректное имя"},
        {"id": 5, "category": "Переводы", "description": "Сидоров С."},
    ]
    expected_result = [
        {"id": 1, "category": "Переводы", "description": "Иванов И."},
        {"id": 3, "category": "Переводы", "description": "Петров П."},
        {"id": 5, "category": "Переводы", "description": "Сидоров С."},
    ]
    result = filter_transactions_to_individuals(transactions)
    assert json.loads(result) == expected_result


def test_filter_transactions_no_matches_individual():
    transactions = [
        {"id": 1, "category": "Покупки", "description": "Товар"},
        {"id": 2, "category": "Покупки", "description": "Еще один товар"},
    ]
    result = filter_transactions_to_individuals(transactions)
    assert json.loads(result) == []


def test_filter_transactions_empty_list_individual():
    transactions = []
    result = filter_transactions_to_individuals(transactions)
    assert json.loads(result) == []


def test_filter_transactions_with_varied_names():
    transactions = [
        {"id": 1, "category": "Переводы", "description": "Смирнов С."},
        {"id": 2, "category": "Переводы", "description": "Петров П."},
        {"id": 3, "category": "Переводы", "description": "Некорректное имя"},
        {"id": 4, "category": "Переводы", "description": "Григорьев Г."},
        {"id": 5, "category": "Переводы", "description": "Иванова И. А."},
    ]
    expected_result = [
        {"id": 1, "category": "Переводы", "description": "Смирнов С."},
        {"id": 2, "category": "Переводы", "description": "Петров П."},
        {"id": 4, "category": "Переводы", "description": "Григорьев Г."},
    ]
    result = filter_transactions_to_individuals(transactions)
    assert json.loads(result) == expected_result
