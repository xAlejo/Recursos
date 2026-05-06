public class Mascota {

    // Atributos
    String nombre;
    private int energia;
    int hambre;

    // Constructor
    public Mascota(String nombre, int energia, int hambre) {
        this.nombre = nombre;
        this.energia = energia;
        this.hambre = hambre;
    }

    // Métodos
    public void jugar() {
        if (energia >= 10) {
            energia -= 10;
            hambre += 5;
            System.out.println(nombre + " ha jugado.");
        } else {
            System.out.println(nombre + " está muy cansada.");
        }
    }

    public void comer() {
        if (hambre > 0) {
            hambre -= 5;
            energia += 5;
            System.out.println(nombre + " ha comido.");
        } else {
            System.out.println(nombre + " no tiene hambre.");
        }
    }

    public void dormir() {
        energia += 15;
        System.out.println(nombre + " ha dormido.");
    }

    public int getEnergia() {
        return energia;
    }

    public void setEnergia(int nuevaEnergia) {
        if (nuevaEnergia >= 0) {
            energia = nuevaEnergia;
        }
    }

    public void mostrarEstado() {
        System.out.println("Mascota: " + nombre);
        System.out.println("Energía: " + energia);
        System.out.println("Hambre: " + hambre);
    }
}
