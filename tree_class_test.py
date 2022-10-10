from datetime import datetime
import timeit


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
    def get_item(self, item_id):
        try:
            for item in self.items:
                if item['id'] == int(item_id):
                    return item
        except Exception as err:
            print(err)

    # Создаём пустой список (A), бежим по нашему списку из конструктора (B) и когда находим элемент со словарём
    # в котором id родителя соответствует переданному id, добавляем этот элемент в пустой список, в конце перебора
    # возвращаем список (A)
    def get_children(self, parent_id):
        children = []
        try:
            for item in self.items:
                if item['parent'] == int(parent_id):
                    children.append(item)
            return children
        except Exception as err:
            print(err)

    # Создаём пустой список (A), бежим по списку из конструктора (B) и когда находим элемент, от которого нужно вернуть
    # всех родителей, вызывает функцию get_parent, после того, как она отработала, возвращаем список (A)
    def get_all_parents(self, child_id):
        parents = []

        # Бежим по контейнеру, добавляем родителя в список (A), смотрим id родителя
        # от родителя и опять вызываем себя уже с новым id родителя
        def get_parent(parent_id, container):
            for item_ in container:
                if item_['id'] == parent_id:
                    parents.append(item_)
                    get_parent(item_['parent'], container)
                    break

        try:
            for item in self.items:
                if item['id'] == int(child_id):
                    get_parent(item['parent'], self.items)
            return parents
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

# start_time = datetime.now()

print(f'get_all(): {ts.get_all()}')
print(f'get_all_parents(7): {ts.get_all_parents(7)}')
print(f'get_item(7): {ts.get_item(7)}')
print(f"get_children(4): {ts.get_children(4)}")
print(f"get_children(5): {ts.get_children(5)}")

# print(datetime.now() - start_time)


code_to_test = """
class TreeStore:

    def __init__(self, items_list: list):
        try:
            self.items = items_list
        except Exception as err:
            print(err)

    def get_all(self):
        try:
            return self.items
        except Exception as err:
            print(err)

    def get_item(self, item_id):
        try:
            for item in self.items:
                if item['id'] == int(item_id):
                    return item
        except Exception as err:
            print(err)

    def get_children(self, parent_id):
        children = []
        try:
            for item in self.items:
                if item['parent'] == int(parent_id):
                    children.append(item)
            return children
        except Exception as err:
            print(err)

    def get_all_parents(self, child_id):
        parents = []

        def get_parent(parent_id, container):
            for item_ in container:
                if item_['id'] == parent_id:
                    parents.append(item_)
                    get_parent(item_['parent'], container)
                    break

        try:
            for item in self.items:
                if item['id'] == int(child_id):
                    get_parent(item['parent'], self.items)
            return parents
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

# оценим время выполнения кода при 100 000 итераций
iterations_number = 100000
print(f'Время выполнения метода get_all_parents в среднем на {iterations_number} итераций: '
      f'{timeit.timeit(code_to_test, number=iterations_number) / iterations_number}')

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},
#  {"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},
#  {"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},
#  {"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
