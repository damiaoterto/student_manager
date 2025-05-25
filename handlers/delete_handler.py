from tui.context import Context


def delete_handler(ctx: Context):
    db = ctx.get_database()

    print("==================================")
    print("========= Deletar aluno ==========")
    print("==================================\n")
    print("\n")
    result = db.select_all('alunos')

    for id, nome, idade in result:
        print(f'[{id}]: {nome} | {idade} anos')
    print("\n")

    id = int(input("Digite o número do aluno: "))
    db.delete_item('alunos', id)
    print("\n")
    input("Precione qualquer tecla para sair...")