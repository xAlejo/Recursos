class Mascota:

    def __init__(self, nombre, energia, hambre):
        self.nombre = nombre
        self.__energia = energia
        self.hambre = hambre
    def jugar(self):
        if self.__energia >= 10:
            self.__energia -= 10
            self.hambre += 5
            print(self.nombre, "ha jugado y ahora tiene", self.__energia,
                "de energía y", self.hambre, "de hambre")
        else:
            print(self.nombre, "está muy cansada para jugar")

    def comer(self):
        if self.hambre > 0:
            self.hambre -= 5
            self.__energia += 5
            print(self.nombre, "ha comido y ahora tiene", self.__energia,
            "de energía y", self.hambre, "de hambre")
        else:
            print(self.nombre, "no tiene hambre")

    def dormir(self):
        self.__energia += 15
        print(self.nombre, "ha dormido y ahora tiene", self.__energia,
            "de energía y", self.hambre, "de hambre")

    def get_energia(self):
        return self.__energia

    def set_energia(self, nueva_energia):
        if nueva_energia < 0:
            print("La energía no puede ser negativa")
        else:
            self.__energia = nueva_energia

    def mostrar_estado(self):
        print("\nMascota:", self.nombre)
        print("Energía:", self.__energia)
        print("Hambre:", self.hambre)
        

print("¡Bienvenido al juego de la mascota virtual!")
print("---------- Reglas del juego: ----------")
print("- Jugar consume 10 de energía y aumenta 5 de hambre.")
print("- Comer reduce 5 de hambre y aumenta 5 de energía.")
print("- Dormir recupera 15 de energía.")

mascota1 = Mascota("Miyu", 50, 20)
mascota2 = Mascota("Nina", 30, 10)

mascota1.mostrar_estado()
mascota1.jugar()
mascota1.comer()
mascota1.dormir()
print("Energía actual:", mascota1.get_energia())

mascota2.mostrar_estado()
mascota2.set_energia(40)
mascota2.jugar()
mascota2.comer()
mascota2.dormir()
print("Energía actual:", mascota2.get_energia())