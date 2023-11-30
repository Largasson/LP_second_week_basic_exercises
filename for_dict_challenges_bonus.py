"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from copy import copy
import lorem
from collections import defaultdict


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def def_value():
    return 0


def search_most_user_id(lst: list):
    """ 1. Вывести айди пользователя, который написал больше всех сообщений. """
    my_dict = defaultdict(int)
    for line in lst:
        my_dict[line['sent_by']] += 1
    return (f'ID пользователя, который написал больше всех сообщений: '
            f'{(max(my_dict.items(), key=lambda item: item[1]))[0]}')


def search_most_reply_user_id(lst: list):
    """ 2. Вывести айди пользователя, на сообщения которого больше всего отвечали. """
    my_dict = defaultdict(int)
    lst_reply_for = {line['reply_for'] for line in lst}
    for r_id in lst_reply_for:
        for line in lst:
            if line['id'] == r_id:
                my_dict[line['sent_by']] += 1
    return (f'ID пользователя, на сообщения которого больше всего отвечали: '
            f'{(max(my_dict.items(), key=lambda item: item[1]))[0]}')


def search_user_id_unic(lst: list):
    """ 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей."""
    my_dict = {}
    for line in lst:
        key = line['sent_by']
        adding = line['seen_by']
        my_dict[key] = my_dict.get(key, []) + adding
    # for k, v in my_dict.items():     чтобы подключить и посмотреть словарь где ключи - айди отправителей,                      !!!!!!!!!!!!!!!!!
    #     print(f'{k}: {set(v)}')           а значения уникальные айди прочитавших пользователей                                !!!!!!!!!!!!!!
    return (f'Получается, что все пользователи видели сообщения друг друга, или я неправильно понял задачу. '
            f'Можно раскоментить словарь внутри функции и посмотреть значения')


def time_research(lst: list):
    """ 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов)."""
    my_dict = defaultdict(int)
    for line in lst:
        if line['sent_at'].hour < 12:
            my_dict['утром'] += 1
        elif 12 <= line['sent_at'].hour <= 18:
            my_dict['днем'] += 1
        else:
            my_dict['вечером'] += 1
    m = max(my_dict.items(), key=lambda item: item[1])[0]
    return f'Больше всего сообщений в чате {m}'


def count_tred(lst: list):
    """ 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов). """
    tred_dict = {line['id']: line['reply_for'] for line in lst}
    lst_message = list(tred_dict.keys())
    message = lst_message.pop()
    count = 0
    search_id = copy(message)
    res = {}
    while message and len(lst_message) > 0:
        if tred_dict[message]:
            count += 1
            message = tred_dict[message]
        else:
            res[search_id] = count
            count = 0
            message = lst_message.pop()
            search_id = copy(message)
    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
    max_count = max(res.items(), key=lambda item: item[1])[1]
    res = dict(filter(lambda item: item[1] == max_count, res.items()))
    answer = []
    for k, v in res.items():
        answer.append(f'ID сообщения, которое является началом самых длинных тредов - {k}. Длина треда - {v}')
    return answer


if __name__ == "__main__":
    lst = generate_chat_history()
    print(search_most_user_id(lst))
    print(search_most_reply_user_id(lst))
    print(search_user_id_unic(lst))
    print(time_research(lst))
    print(*count_tred(lst), sep='\n')
