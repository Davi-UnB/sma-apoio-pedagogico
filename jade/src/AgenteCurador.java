import jade.core.Agent;

public class AgenteCurador extends Agent {
    @Override
    protected void setup() {
        System.out.println("Olá! O agente curador " + getAID().getName() + " está pronto.");
    }
}

