# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44
disk_size_b = disk_size_mb * 1024 * 1024
pages = 100
lines = 50
symbols = 25
symbol_size_b = 4
book_size_b = pages * lines * symbols * symbol_size_b
number_of_books = disk_size_b // book_size_b
print("Количество книг, помещающихся на дискету:", int(number_of_books))
