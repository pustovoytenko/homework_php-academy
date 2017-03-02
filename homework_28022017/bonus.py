_dict1 = {
    1: "one",
    "two": 2
}
_list1 = [101, False, "Hello", [3, 4, 5], _dict1]

print(_list1)
print(_list1[0])
print(_list1[1])
print(_list1[2])
print(_list1[3])
print(_list1[4])

a = "123.456"

b = float(a)
print(type(b), b)

c = '{}{}{}'.format(a[0], a[1], a[2])
c = int(c)
print(type(c), c)