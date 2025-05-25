from tui.context import Context


def insert_handler(ctx: Context):
    db = ctx.get_database()

    print("==================================")
    print("========= Inserir aluno ==========")
    print("==================================\n")

    name = input("Nome: ")
    age = input("Idade: ")
    db.insert_item('alunos', ['nome', 'idade'], (name, age))
    input("Precione qualquer tecla para sair...")