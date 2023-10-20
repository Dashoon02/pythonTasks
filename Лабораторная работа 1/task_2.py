# TODO Найдите количество книг, которое можно разместить на дискете
max_weight = 1.44 #Мб
pages = 100
lines_on_one_page = 50
number_in_one_line = 25

weight_of_one_number = 4 #байта
max_weight *= 1024*1024   #теперь измеряем в байтах
count_of_number = pages*lines_on_one_page*number_in_one_line
weight_of_one_book = count_of_number*weight_of_one_number
total = int(max_weight//weight_of_one_book)

print("Количество книг, помещающихся на дискету:", total)
