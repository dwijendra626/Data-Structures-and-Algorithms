def linearSearch(list, value):
        for i in range(len(list)):
            if list[i] == value:
                    return True
        return -1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 20
print(linearSearch(list, item))