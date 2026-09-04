import jade.core.Agent;

public class MeuPrimeiroAgente extends Agent {
    @Override
    protected void setup() {
        System.out.println("Olá! O agente " + getAID().getName() + " está pronto.");
    }
}