# Проект по Python

## Описание:

Курсовой проект по Python - это приложение для анализа транзакций, которые находятся в Excel-файле. Приложение будет генерировать JSON-данные для веб-страниц, формировать Excel-отчеты, а также предоставлять другие сервисы.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://yuliyakuznetsova0102/KursPy1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Функция filter_transactions_with_phone_numbers возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера
2. Функция filter_transactions_to_individuals возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам
3. Функция greetings_time - приветствие в формате "???", где ??? — «Доброе утро» / «Добрый день» / 
    «Добрый вечер» / «Доброй ночи» в зависимости от текущего времени
4. Функция get_card_data. которая возвращает json ответ по каждой карте:последние 4 цифры карты; общая сумма расходов;
    кешбэк (1 рубль на каждые 100 рублей).
5. Функция get_top_transactions, которая возвращающает json-ответ с топ-5 транзакций по сумме платежа
6. Функция get_currency_rates, которая возвращающет json-ответ о курсе валют.
7. Функция get_sp500_stock_prices, которая возвращающает json - ответ о стоимости акций из S&P500
8. 
9. 
10. 
11. 
12. 
13. 
14.  


## Тестирование:

Для запуска тестирования необходимо в терминале ввести "pytest"
