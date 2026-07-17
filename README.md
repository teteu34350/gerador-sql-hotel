# 🚀 Gerador SQL - Sistema IO

Aplicação desktop desenvolvida em Python para facilitar a geração automática de scripts SQL a partir de arquivos Excel.

O sistema permite selecionar um hotel, importar uma planilha, escolher a aba desejada e gerar comandos SQL de manutenção automaticamente.

---

## 📌 Funcionalidades

✅ Seleção de hotel  
✅ Busca automática do ID do hotel  
✅ Importação de arquivos Excel (`.xlsx`)  
✅ Listagem de abas visíveis da planilha  
✅ Escolha da aba para leitura dos dados  
✅ Processamento das informações da planilha  
✅ Geração automática de comandos SQL  
✅ Visualização do SQL gerado  
✅ Botão para copiar SQL  

---

## 🖥️ Interface

O sistema possui uma interface gráfica desenvolvida utilizando:

- CustomTkinter
- Tkinter

Com modo escuro e componentes modernos.

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- CustomTkinter
- Pandas
- OpenPyXL
- Git/GitHub

---

## 📂 Estrutura do projeto

```
Gerador-SQL/
│
├── gui.py                 # Interface principal do sistema
├── excel_reader.py        # Leitura e tratamento das planilhas Excel
├── hotel_manager.py       # Gerenciamento dos hotéis e IDs
├── sql_generator.py      # Geração dos comandos SQL
│
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação
└── .gitignore
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Gerador-SQL
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o projeto

Execute:

```bash
python gui.py
```

---

## 📄 Exemplo de funcionamento

Fluxo do sistema:

```
Selecionar Hotel
        ↓
Selecionar arquivo Excel
        ↓
Carregar abas disponíveis
        ↓
Escolher aba da planilha
        ↓
Processar dados
        ↓
Gerar SQL
        ↓
Copiar resultado
```

---

## 📦 Gerando executável

Para gerar uma versão `.exe`:

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Execute:

```bash
pyinstaller --onefile --windowed --name "Gerador_SQL_Sistema_IO" gui.py
```

O executável será criado na pasta:

```
dist/
└── Gerador_SQL_Sistema_IO.exe
```

---

## 🔒 Observações

- O sistema necessita das planilhas Excel no formato esperado pelo gerador.
- As abas ocultas das planilhas são ignoradas.
- A estrutura dos dados deve seguir o padrão configurado no sistema.

---

## 👨‍💻 Desenvolvimento

Desenvolvido por:

**Matheus Santana**  
Sistema IO

---

⭐ Projeto desenvolvido para otimizar processos internos e reduzir tarefas manuais.

<img width="902" height="675" alt="image" src="https://github.com/user-attachments/assets/32f824fb-e1d3-4cdf-9829-29d02b0d5170" />
