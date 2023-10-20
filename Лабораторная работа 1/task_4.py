users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
unique_users = set(users)
dictionary = {
"Общее количество": len(users),
"Уникальные посещения": len(unique_users)
}
print(dictionary)