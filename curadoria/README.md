# Módulo de Curadoria

Este módulo é responsável pela conversão de materiais didáticos para o formato Markdown. A fim de alimentar um RAG(Retrieval-Augmented Generation)

---

## 📁 Estrutura de Diretórios

```text
curadoria/
├── .gitignore
├── README.md
├── requirements.txt
├── materiais/             # ⚠️ Deve ser criada manualmente (ignorada pelo git)
│   └── documento.pdf
└── extracao/
    ├── extrator_pdf.py    # Script principal de conversão
    └── saidas/            # Saída gerada (.md e imagens)
```

> **Atenção:** As pastas `curadoria/materiais/` e `curadoria/extracao/saidas/` estão no `.gitignore` para evitar envio de arquivos pesados ou dados brutos ao repositório.

---

## 🚀 Como Usar

### 1. Pré-requisitos e Instalação

Certifique-se de ter o ambiente virtual ativo (criado na raiz do repositório conforme o [README principal](../README.md)) e instale as dependências:

```bash
# Na pasta curadoria/
pip install -r requirements.txt
```

### 2. Criar a pasta de materiais e inserir os arquivos

Crie a pasta `materiais` dentro de `curadoria/` (caso ainda não exista) e copie seus arquivos PDF para ela:

```bash
mkdir -p materiais
```

Em seguida, adicione os arquivos `.pdf` que você deseja processar dentro de `curadoria/materiais/`.

### 3. Executar a Extração

Navegue até a pasta `extracao/` e execute o script:

```bash
cd extracao
python extrator_pdf.py
```

### 4. Resultados

Os arquivos convertidos serão gerados automaticamente na pasta `curadoria/extracao/saidas/`:
- Documento `.md` contendo o texto extraído pronto para chunking e vetorização.
- Figuras e diagramas recortados em alta resolução e referenciados no próprio Markdown.
