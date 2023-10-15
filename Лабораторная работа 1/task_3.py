list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)//2
team1 = list_players[:count]
team2 = list_players[count:]
print(team1)
print(team2)