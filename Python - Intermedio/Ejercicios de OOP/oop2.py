import random

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def board_bus(self, person):
        if len(self.passengers) >= self.max_passengers:
            print("Ya se alcanzó la capacidad de carga del bus. No se permiten más personas.")
        else: 
            self.passengers.append(person)
            print (f"{person.name} se subió al bus.")

    def drop_passenger(self):
        if len(self.passengers) <= 0:
            print("Ya se bajaron todas los pasajeros.")
        else: 
            passenger_dropped = self.passengers.pop(random.randrange(len(self.passengers)))
            print (f"Se bajó {passenger_dropped.name}.")

passenger1 = Person("Abigail", 26)
passenger2 = Person("Verónica", 45)
passenger3 = Person("Warren", 43)
bus1 = Bus(2)
bus1.board_bus(passenger1)
bus1.board_bus(passenger2)
bus1.board_bus(passenger3)
bus1.drop_passenger()
bus1.drop_passenger()
bus1.drop_passenger()
