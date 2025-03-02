class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод!")


class Car(Vehicle):
    def drive(self):
        print("Машина едет...")
        self.engine.start()
        print("Едем на машине.")
        self.engine.stop()

class Bike(Vehicle):
    def drive(self):
        print("Велосипед в пути...")
        self.engine.start()
        print("Едем на велосипеде.")
        self.engine.stop()


class Engine:
    def start(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод!")

    def stop(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод!")

class GasolineEngine(Engine):
    def start(self):
        print("Бензиновый двигатель запускается... ")

    def stop(self):
        print("Бензиновый двигатель останавливается... ")

class ElectricEngine(Engine):
    def start(self):
        print("Электрический двигатель запускается... ")

    def stop(self):
        print("Электрический двигатель останавливается... ")

class HybridEngine(Engine):
    def start(self):
        print("Гибридный двигатель запускается... ")

    def stop(self):
        print("Гибридный двигатель останавливается... ")


def main():

    gasoline_car = Car(GasolineEngine())
    electric_bike = Bike(ElectricEngine())
    hybrid_car = Car(HybridEngine())


    gasoline_car.drive()
    print()
    electric_bike.drive()
    print()
    hybrid_car.drive()

if __name__ == "__main__":
    main()