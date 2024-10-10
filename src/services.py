import json
import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="services.log",
    filemode="w",
)
services_logger = logging.getLogger("services")


def filter_transactions_with_phone_numbers(transactions: list[dict]) -> str:
    """Функция возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера."""
    phone_pattern = re.compile(r"(?:(?:\+7|8)\s?)?(?:\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{2}[\s-]?\d{2}")
    filtered_transactions = [
        transaction
        for transaction in transactions
        if "description" in transaction and phone_pattern.search(transaction["description"])
    ]
    services_logger.info("В транзакции сть номер телефона")
    return json.dumps(filtered_transactions, ensure_ascii=False)


def filter_transactions_to_individuals(transactions: list[dict]) -> str:
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам."""
    name_pattern = re.compile(r"^[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.$")
    filtered_transactions = [
        transaction
        for transaction in transactions
        if (
            transaction.get("category") == "Переводы"
            and "description" in transaction
            and name_pattern.search(transaction["description"])
        )
    ]
    services_logger.info("В транзакции присутствует превод физическому лицу")
    return json.dumps(filtered_transactions, ensure_ascii=False)
