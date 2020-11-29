from ua.univer.lesson.lesson06.pet.pet_class import Pet


def main():
    name = input("Enter name ")
    animal_type = input("Enter animal type ")
    age = input("Enter age ")
    pet1 = Pet(name, animal_type, age)
    pet1.show()
    pet1.set_name(name)
    pet1.set_animal_type(animal_type)
    pet1.set_age(age)
    print(pet1.get_name(name))
    print(pet1.get_animal_type(animal_type))
    print(pet1.get_age(age))


main()
