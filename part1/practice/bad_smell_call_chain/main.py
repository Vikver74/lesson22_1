# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

class Person:
    def __init__(self, city: str, street: str, room: int):
        self.city = city
        self.street = street
        self.room = room

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_room(self):
        return self.room


if __name__ == '__main__':
    person = Person('Kursk', 'Lenina', 42)
    print(person.get_city())
    print(person.get_street())
    print(person.get_room())
