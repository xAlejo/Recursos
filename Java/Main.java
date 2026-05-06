
public class Main {
    public static void main(String[] args) {

        Mascota mascota1 = new Mascota("Miyu", 50, 20);
        Mascota mascota2 = new Mascota("Nina", 30, 10);

        mascota1.mostrarEstado();
        mascota1.jugar();
        mascota1.comer();
        mascota1.dormir();

        System.out.println("Energía actual: " + mascota1.getEnergia());

        mascota2.mostrarEstado();
        mascota2.setEnergia(40);
        mascota2.jugar();
        mascota2.comer();
        mascota2.dormir();

        System.out.println("Energía actual: " + mascota2.getEnergia());
    }
}
