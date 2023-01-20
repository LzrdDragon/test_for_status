import timeit


code_to_test = """
from sys import setrecursionlimit


class TreeStore:
    # Конструктор
    def __init__(self, items_list: list):
        try:
            self.items = items_list
        except Exception as err:
            print(err)

    # Просто возвращаем список из конструктора
    def get_all(self):
        try:
            return self.items
        except Exception as err:
            print(err)

    # Бежим по списку и проверяем id на соответствие переданному, при соответствии возвращаем
    def get_item(self, item_id: int):
        try:
            for item in self.items:
                if item['id'] == int(item_id):
                    return item
        except Exception as err:
            print(err)

    # Создаём пустой список (children), бежим по нашему списку из конструктора (self.items) и когда находим элемент
    # со словарём в котором id родителя соответствует переданному id, добавляем этот элемент в пустой список,
    # в конце перебора возвращаем список (children)
    def get_children(self, parent_id):
        children = []
        try:
            for item in self.items:
                if item['parent'] == int(parent_id):
                    children.append(item)
            return children
        except Exception as err:
            print(err)

    # Создаём пустой список (_parents), бежим по списку из конструктора (self.items) и когда находим элемент,
    # от которого нужно вернуть всех родителей, вызываем функцию get_parent, после того, как она отработала,
    # возвращаем список (_parents)
    def get_all_parents(self, child_id):
        _parents = []

        # Бежим по контейнеру, добавляем родителя в список (children), смотрим id родителя
        # от родителя и опять вызываем себя уже с новым id родителя
        def get_parent(parent_id: int = None, container: list = None, parents: list = None):
            for item_ in container:
                if item_['id'] == parent_id:
                    parents.append(item_)
                    get_parent(item_['parent'], container, parents)
                    break

        try:
            for item in self.items:
                if item['id'] == int(child_id):
                    setrecursionlimit(len(self.items) + 10)
                    get_parent(item['parent'], self.items, _parents)
                    break
            return _parents
        except Exception as err:
            print(err)


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
ts.get_all_parents(7)
"""

# оценим время выполнения по функции get_all_parents(7) при 100 000 итераций
iterations_number = 100000
print(f'Время выполнения метода get_all_parents в среднем на {iterations_number} итераций: '
      f'{timeit.timeit(code_to_test, number=iterations_number)} секунд')
