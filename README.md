## Gerenciador de Estudantes
Um simples aplicativo de terminal para gerenciar um banco de dados de estudantes.

### Visão Geral
Este projeto é um sistema de gerenciamento de estudantes baseado em texto (TUI - Text User Interface) que permite ao usuário realizar operações básicas de CRUD (Criar, Ler, Atualizar, Excluir) em um banco de dados de estudantes. A aplicação é desenvolvida em Python e utiliza um banco de dados SQLite para persistência dos dados.

### Funcionalidades
O menu principal da aplicação oferece as seguintes opções:
-   **Incluir**: Adiciona um novo estudante ao banco de dados.
-   **Listar**: Exibe todos os estudantes cadastrados.
-   **Atualizar**: Modifica os dados de um estudante existente.
-   **Excluir**: Remove um estudante do banco de dados.
-   **Sair**: Encerra a aplicação.

### Estrutura do Projeto
O projeto é organizado nos seguintes diretórios e arquivos:
-   `app.py`: Contém a classe principal da aplicação que inicializa o contexto e o menu.
-   `main.py`: Ponto de entrada da aplicação.
-   `infra/`: Contém a lógica de interação com o banco de dados.
    -   `database.py`: Gerencia a conexão e as operações no banco de dados SQLite.
-   `handlers/`: Contém as funções que manipulam as ações do menu.
    -   `insert_handler.py`: Lida com a inserção de novos estudantes.
    -   `list_handler.py`: Lida com a listagem dos estudantes existentes.
    -   `update_handler.py`: Lida com a atualização das informações dos estudantes.
    -   `delete_handler.py`: Lida com a exclusão de estudantes.
-   `tui/`: Contém os componentes da interface de usuário do terminal.
    -   `menu.py`: Cria e exibe o menu de navegação.
    -   `context.py`: Mantém o estado da aplicação, como a conexão com o banco de dados.
-   `utils/`: Contém funções utilitárias.
    -   `colorize.py`: Adiciona cores ao texto do terminal.
    -   `terminal.py`: Fornece a funcionalidade de limpar a tela do terminal.

### Execução
Execute o seguinte comando no diretório raiz do projeto:
```python
python main.py
```

Um arquivo de banco de dados `db.sqlite` será criado no mesmo diretório.