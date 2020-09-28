from collections import OrderedDict


class User:
    """
    обладает всеми необходимыми пользовательскими методами, например показать задачи
    пользователя, отсортировать по приоритету и т.д.
    """
    def __init__(self):
        pass

    @classmethod
    def convert_find(cls, input_list: list) -> list:
        """
        Функция принимает на вход необработанныей вывод поиска в базе за определенную дату
        Выводит отсортированный список задач
        :param input_list:
        :return:
        """
        result = [i[1] for i in input_list]
        return sorted(result)

    @classmethod
    def format_all(cls, output_list: list) -> dict:
        """
        Метод на вход получает список
        Возвращает словарь дата: список задач
        :param output_list:
        :return:
        """
        result = OrderedDict()
        for i in output_list:
            date = list(i)[0]
            task = list(i)[1]
            if date in result.keys():
                result[date].append(task)
            else:
                result[date] = [task, ]
        for value in result.values():
            value.sort()
        return result


    @classmethod
    def convert_data(cls, data: str) -> str:
        """
        Метод преобразует, введеную пользователем дату к виду 000y-0m-0d,
        заполняя недостающие цифры нулями
        :param data:
        :return:
        """
        to_change = data.split('-')
        year = to_change[0]
        month = to_change[1]
        day = to_change[2]
        return f"{year.rjust(4, '0')}-{month.rjust(2, '0')}-{day.rjust(2, '0')}"