my_dictionary = {
    "first_name": "Chris",
    "last_name": "Paulysta",
    "email": "qwerty@n.ua",
    "age": 25
}

my_list = []
list_range = []

# generate list from range [25-40]
for i in range(25, 41):
    list_range.append(i)

for e in my_dictionary.values():

    if type(e) is str and len(e) > 5 and e.find("a") != -1:
        my_list.append(e)
    elif type(e) is int and list_range.count(e) == 1:
        my_list.append(e)
    else:
        pass
print(my_list)

for not_nm in my_list:
    if type(not_nm) is str:
        if not_nm.find("n") != -1 or not_nm.find("m") != -1:
            my_list.remove(not_nm)
    else:
        pass
print(my_list, "\n")

# sort list Z-A
za_list = ["Katya", "Lena", "Anna", "Zina"]
za_list.sort(reverse=True)
print(za_list, "\n")

# convert list to string
new_string = ','.join(za_list)
print(new_string, "\n")

# reverse string
list_is_back = new_string.split(',')
print(list_is_back, "\n")

from module import check_type
print(check_type("qwerty"))

from random import randint
rand_num = randint(10, 20)

for a in range(0, rand_num):
    check_type(1)
