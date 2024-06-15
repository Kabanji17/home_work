origin_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
               ]


def filter_by_state(origin_list: list[dict[str, str | int]], state: str='EXECUTED') -> list[dict[str, str | int]]:
    """ Функция, сортирующая список по введенному ключу"""
    filtered_list = []
    for data in origin_list:
        if data.get("state") == state:
            filtered_list.append(data)
    return filtered_list


def