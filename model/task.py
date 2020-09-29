import sqlite3


class Task:
    """
    хранит в себе все необходимые методы для создания, сохранения, изменения
    (изменения состояния) задач, а так же их удаления (пометки "выполнено")
    """
    __tablename__ = "tasks"
    __database__ = 'tasks.db'

    def __init__(self, data: str, task: str):
        self.__data = data
        self.__task = task
        self.__status = True
        self.__save()

    def __save(self) -> None:
        '''
        Метод сохраняет дату и задание со статусом True
        Проверяет на наличие пары дата: задание в базе
        :return:
        '''
        if not self.check_data_event(self.__data, self.__task):
            conn = sqlite3.connect(self.__database__)
            cur = conn.cursor()

            query_save = f'INSERT INTO {self.__tablename__} VALUES(?, ?, ?)'
            cur.execute(query_save, (self.__data, self.__task, self.__status))

            conn.commit()
            conn.close()

    @classmethod
    def del_task(cls, data: str, task: str):
        """
        Метод изменяет статус задания на False (выполнено)
        :param data:
        :param event:
        :return:
        """
        if cls.check_data_event(data, task):
            conn = sqlite3.connect(cls.__database__)
            cur = conn.cursor()

            query_edit_status = f'UPDATE {cls.__tablename__} SET status=? WHERE data=? AND task=? AND status=True'
            cur.execute(query_edit_status, (False, data, task))

            conn.commit()
            conn.close()
        else:
            raise ValueError

    @classmethod
    def del_date(cls, data: str):
        """
        Метод переводит все задачи за указанную дату в стостояние False
        :param data:
        :return:
        """
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_edit_status = f'UPDATE {cls.__tablename__} SET status=? WHERE data=? AND status=True'
        query_count = f'SELECT COUNT(status) FROM {cls.__tablename__} WHERE data=? AND status=True'
        result = list(cur.execute(query_count, (data,)))
        cur.execute(query_edit_status, (False, data))

        conn.commit()
        conn.close()
        # Декапсулирую результат из кортежа и списка [(int,)]
        result = result[0][0]
        return result

    @classmethod
    def check_data_event(cls, data: str, task: str) -> bool:
        """
        Метод проверяет существует пара дата: задание или не существует
        :return:
        """
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_check = f"SELECT * FROM {cls.__tablename__} WHERE data=? AND task=? AND status=True"
        result = list(cur.execute(query_check, (data, task)))
        conn.close()
        return len(result) > 0

    @classmethod
    def find_data(cls, data: str) -> str:
        """
        Метод ищет все задания за указанную дату и выводит результат в виде списка
        :param data:
        :return:
        """
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_find = f'SELECT * FROM {cls.__tablename__} WHERE data=? AND status=True'
        result = list(cur.execute(query_find, (data,)))

        conn.close()
        return result

    @classmethod
    def print_all(cls):
        """
        Метод выводит список всех кортежей с датой, задачей,
        :return:
        """
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_select = f'SELECT data, task FROM {cls.__tablename__} ORDER BY data'
        result = list(cur.execute(query_select))

        conn.close()
        return result

    @classmethod
    def get_active_done_tasks(cls, status):
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_select = f'SELECT data, task FROM {cls.__tablename__} WHERE status=? ORDER BY data'
        result = list(cur.execute(query_select, (status, )))

        conn.close()
        return result
