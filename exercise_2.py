origin_list = [1, 2, 4, 5, 6, 9, 7]
for number in range(1, len(origin_list)):
    if origin_list[number] != origin_list[number - 1] + 1:
        print(origin_list[number])
