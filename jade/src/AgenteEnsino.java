import jade.core.Agent;

public class AgenteEnsino extends Agent {
    @Override
    protected void setup() {
        System.out.println("Olá! O agente de ensino " + getAID().getName() + " está pronto.");
    }
}