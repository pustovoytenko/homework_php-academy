class Animal(object):
    is_alive = True

    def __init__(self, is_big, age, weight):
        # self.alive = is_alive
        self.is_big = is_big
        self.age = age
        self.weight = weight


class Cats(Animal):

    def voice(self):
        return "Meow"


class Dogs(Animal):

    def voice(self):
        return "Woof"


class Foxes(Animal):
    pass

cat = Cats(False, 5, 2)\
dog = Dogs(False, 3, 5)
tiger = Cats(True, 6, 50)
wolf = Dogs(True, 7, 30)
fox = Foxes(False, 4, 6)


def check_voice(animal):
    try:
        print(animal.voice())
    except AttributeError:
        print("This animal has no voice")

# cat.voice()
# dog.voice()
# tiger.voice()
# wolf.voice()
# fox.voice()

check_voice(cat)
check_voice(dog)
check_voice(fox)
check_voice(wolf)
check_voice(tiger)