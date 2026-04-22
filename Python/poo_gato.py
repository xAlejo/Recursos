#Parte 1

class Gato:
    def hablar(self):
        print("Miau, soy un gato")

Atigrado=Gato()
Atigrado.hablar()

Gris=Gato()
Gris.hablar()

# Parte 2

class Gato:
    color="default"
    def hablar(self):
        print(f"Miau, soy un gato de color {self.color}")
    
Atigrado=Gato()
Atigrado.color="café"
Atigrado.hablar()

Gris=Gato()
Gris.color="gris"
Gris.hablar()