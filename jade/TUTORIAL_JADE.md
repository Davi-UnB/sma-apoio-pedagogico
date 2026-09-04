# 🤖 Guia Prático e Tutorial JADE (Java Agent Development Framework)

Este guia serve como referência rápida e completa para o desenvolvimento, compilação, execução e depuração de sistemas multiagentes com JADE neste repositório.

---

## 📁 1. Estrutura do Repositório

```text
untitled/
├── src/
│   ├── MeuPrimeiroAgente.java   # Exemplo de agente JADE implementado
│   └── Main.java                # Classe padrão (não utilizada pelo JADE)
├── lib/
│   ├── jade.jar                 # Biblioteca principal do JADE (runtime e classes base)
│   └── jadeExamples.jar         # Exemplos oficiais da plataforma
├── bin/ ou out/                 # Arquivos compilados (.class)
├── APDescription.txt            # Gerado automaticamente pelo Main-Container do JADE
├── MTPs-Main-Container.txt      # Endereços MTP gerados automaticamente
└── TUTORIAL_JADE.md             # Este guia de consulta
```

---

## ☕ 2. Gerenciando Versões do Java (macOS)

Este ambiente possui duas versões principais do Java:
* **Java 8 (Zulu 1.8.0_492)**: `/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home` *(Recomendada para JADE por compatibilidade total)*
* **Java 25 (OpenJDK 25.0.3)**: `/opt/homebrew/Cellar/openjdk@25/25.0.3/libexec/openjdk.jdk/Contents/Home`

### Como alternar no Terminal:

* **Usar Java 8 na sessão atual do terminal:**
  ```bash
  export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
  java -version
  ```

* **Voltar para o Java 25:**
  ```bash
  export JAVA_HOME=$(/usr/libexec/java_home -v 25)
  java -version
  ```

* **Executar diretamente com o binário do Java 8 (sem exportar):**
  ```bash
  /Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home/bin/java -version
  ```

---

## 💻 3. Como Rodar pelo Terminal

O JADE é iniciado através de sua classe de boot (`jade.Boot`), informando o classpath que inclui o `jade.jar` e a pasta com suas classes compiladas.

### Passo 1: Compilar os Agentes
Crie uma pasta de saída (ex: `bin`) e compile todos os fontes em `src/`:

```bash
mkdir -p bin
javac -cp "lib/jade.jar" -d bin src/*.java
```

### Passo 2: Executar

#### A. Main Container com Interface Gráfica (RMA) + 1 Agente
```bash
java -cp "lib/jade.jar:bin" jade.Boot -gui agente1:MeuPrimeiroAgente
```

#### B. Instanciar múltiplos agentes
Separe as definições de agentes por ponto e vírgula `;`:
```bash
java -cp "lib/jade.jar:bin" jade.Boot -gui "agente1:MeuPrimeiroAgente;agente2:MeuPrimeiroAgente"
```

#### C. Passar parâmetros para os agentes
Argumentos são passados entre parênteses e separados por vírgula:
```bash
java -cp "lib/jade.jar:bin" jade.Boot -gui "comprador:MeuPrimeiroAgente(livro-java,50)"
```
*(No código Java, recupere com: `Object[] args = getArguments();`)*

#### D. Rodar sem Interface Gráfica (Modo Headless / Servidor)
Basta omitir a flag `-gui`:
```bash
java -cp "lib/jade.jar:bin" jade.Boot agente1:MeuPrimeiroAgente
```

#### E. Subir um Container Secundário (Distribuído)
Em outra janela de terminal (na mesma máquina ou em outra máquina da rede):
```bash
java -cp "lib/jade.jar:bin" jade.Boot -container agenteRemoto:MeuPrimeiroAgente
```
*Se o Main-Container estiver em outra máquina na rede:*
```bash
java -cp "lib/jade.jar:bin" jade.Boot -container -host <IP_DO_MAIN_CONTAINER> -port 1099 agenteRemoto:MeuPrimeiroAgente
```

---

## 🛠️ 4. Como Rodar e Depurar pelo IntelliJ IDEA

### Configurando o SDK do Projeto:
1. Abra o menu **File** > **Project Structure...** (atalho `Cmd + ;`).
2. Na aba **Project**, no campo **SDK**, selecione `1.8 (Zulu)`.
3. Clique em **Apply** e **OK**.

### Criando a Configuração de Execução (Run Configuration):
1. No menu superior, vá em **Run** > **Edit Configurations...**.
2. Clique no botão **`+`** (Add New Configuration) e selecione **Application**.
3. Configure os seguintes campos:
   * **Name**: `JADE - Main Container`
   * **JDK**: `1.8` (ou o JDK padrão do projeto)
   * **Main class**: `jade.Boot`
   * **Program arguments**: `-gui agente1:MeuPrimeiroAgente`
   * **Classpath of module**: `MultiAgente`
4. Clique em **Apply** e **OK**.

> **Dica de Debug:** Agora você pode clicar no ícone de inseto (**Debug**) ou pressionar `Shift + F9`. Coloque breakpoints dentro do método `setup()` ou dentro de qualquer `Behaviour` para inspecionar variáveis e mensagens passo a passo.

---

## 📜 5. Cheat Sheet de Código JADE

### Estrutura Base de um Agente
```java
import jade.core.Agent;

public class ExemploAgente extends Agent {

    @Override
    protected void setup() {
        System.out.println("Agente " + getAID().getName() + " iniciando...");

        // Lendo argumentos passados na linha de comando
        Object[] args = getArguments();
        if (args != null && args.length > 0) {
            String parametro = (String) args[0];
            System.out.println("Argumento recebido: " + parametro);
        }

        // Adicionando um comportamento
        // addBehaviour(new MeuComportamento());
    }

    @Override
    protected void takeDown() {
        System.out.println("Agente " + getAID().getName() + " finalizando.");
    }
}
```

### Principais Tipos de Comportamento (Behaviours)

| Comportamento | Classe Base | Uso Comum |
| :--- | :--- | :--- |
| **Execução Única** | `OneShotBehaviour` | Tarefas de inicialização, envio de uma única mensagem pontual. |
| **Execução Cíclica** | `CyclicBehaviour` | Escuta contínua de mensagens recebidas na fila. |
| **Execução Periódica** | `TickerBehaviour` | Tarefas repetidas a cada $X$ milissegundos (ex: verificar status a cada 5s). |
| **Execução Agendada** | `WakerBehaviour` | Executa uma ação após uma espera de $X$ milissegundos. |

#### Exemplo: Recebendo Mensagens com `CyclicBehaviour`
```java
import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;

addBehaviour(new CyclicBehaviour(this) {
    @Override
    public void action() {
        ACLMessage msg = myAgent.receive();
        if (msg != null) {
            System.out.println("Mensagem de " + msg.getSender().getName() + ": " + msg.getContent());
            
            // Responder:
            ACLMessage reply = msg.createReply();
            reply.setPerformative(ACLMessage.INFORM);
            reply.setContent("Mensagem recebida com sucesso!");
            myAgent.send(reply);
        } else {
            block(); // Bloqueia até chegar uma nova mensagem para não consumir 100% de CPU
        }
    }
});
```

#### Exemplo: Enviando Mensagem com `OneShotBehaviour`
```java
import jade.core.AID;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;

addBehaviour(new OneShotBehaviour() {
    @Override
    public void action() {
        ACLMessage msg = new ACLMessage(ACLMessage.INFORM);
        msg.addReceiver(new AID("agente2", AID.ISLOCALNAME));
        msg.setContent("Olá, agente2!");
        send(msg);
    }
});
```

---

## ⚡ 6. Script de Atalho (`run.sh`)

Para compilar e rodar com um único comando no terminal, você pode usar um script shell:

```bash
./run.sh
```
Ou passando agentes personalizados:
```bash
./run.sh "agente1:MeuPrimeiroAgente;agente2:MeuPrimeiroAgente"
```
