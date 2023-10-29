# TODO Напишите функцию для поиска индекса товара
def find_index_of_product(list_of_items, item_to_find):
    for index_of_product in range(len(list_of_items)):
        if item_to_find == list_of_items[index_of_product]:
            return index_of_product


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_of_product(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
