#!/bin/zsh

# Configura para usar o Java 8 (Zulu) se disponível no Mac
if /usr/libexec/java_home -v 1.8 >/dev/null 2>&1; then
    export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
fi

echo "==========================================="
echo "☕ Java em uso: $(java -version 2>&1 | head -n 1)"
echo "==========================================="

# 1. Compila os arquivos fonte para a pasta bin
echo "🔨 Compilando fontes em src/..."
mkdir -p bin
javac -cp "lib/jade.jar" -d bin src/*.java

if [ $? -ne 0 ]; then
    echo "❌ Erro durante a compilação."
    exit 1
fi

# 2. Define os agentes (usa o primeiro argumento do script ou o padrão)
AGENTES=${1:-"agente1:MeuPrimeiroAgente"}

echo "🚀 Iniciando JADE com agentes: $AGENTES"
echo "==========================================="
java -cp "lib/jade.jar:bin" jade.Boot -gui "$AGENTES"
