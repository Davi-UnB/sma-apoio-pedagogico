# 🎓 Sistema Multiagente de Apoio Pedagógico para Ecossistema de Universidade Virtual

---

## 🐍 Configuração do Ambiente Virtual (Python)

Para rodar os módulos Python do projeto (como o módulo de curadoria e extração), utilize um ambiente virtual (`venv`) criado na raiz do repositório para isolar todas as dependências:

### 1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 2. Ativar o ambiente virtual

- **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- **Windows (CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

### 3. Atualizar o gerenciador de pacotes (opcional, mas recomendado)

```bash
pip install --upgrade pip
```

### 4. Desativar o ambiente virtual

Quando terminar de trabalhar no projeto:

```bash
deactivate
```
