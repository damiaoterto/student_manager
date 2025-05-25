from tui.context import Context


def update_handler(ctx: Context):
    db = ctx.get_database()

    print("==================================")
    print("========= Atualizar aluno ==========")
    print("==================================\n")
    print("\n")
    result = db.select_all('alunos')

    for id, nome, idade in result:
        print(f'[{id}]: {nome} | {idade} anos')
    print("\n")

    id = int(input("Digite o número do aluno: "))
    nome = input("Digite o nome do aluno: ")
    age = int(input("Digite o idade do aluno: "))
    db.update_item('alunos', ['nome', 'idade'], (nome, age), id)
    print("\n")
    input("Precione qualquer tecla para sair...")