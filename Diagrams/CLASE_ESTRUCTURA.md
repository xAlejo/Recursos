
classDiagram
class Mascota {
    +str nombre
    -int energia
    +int hambre
    +jugar() void
    +comer() void
    +dormir() void
    +get_energia() int
    +set_energia(nueva_energia : int) void
    +mostrar_estado() void
}
