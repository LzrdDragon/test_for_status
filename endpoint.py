from tree_class import TreeStore


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

print(f'get_all(): {ts.get_all()}')
print(f'get_all_parents(7): {ts.get_all_parents(7)}')
print(f'get_item(7): {ts.get_item(7)}')
print(f"get_children(4): {ts.get_children(4)}")
print(f"get_children(5): {ts.get_children(5)}")
