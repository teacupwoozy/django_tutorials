pretty_colors = {
    'color': 'purple',
    'amount': 14,
    'animal': 'panda'
}

happy_animales = ['cats', 'bats', 'rats']

happy_numbers = [1, 2, 33, 473]


print(happy_animales)
totes = sum(happy_numbers)

print(totes)

if 3 > 2:
    print("yes!")
else:
    print("nope")


def hi(animal):
    print("¿Qué pasa " + animal + "?")

# hi()


for animal in happy_animales:
    hi(animal)