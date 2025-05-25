from tui.context import Context

def list_handler(ctx: Context):
    db = ctx.get_database()

    print("====================================")
    print("========= Lista de alunos ==========")
    print("====================================\n")

    result = db.select_all('alunos')

    for id, nome, idade in result:
        print(f'[{id}]: {nome} | {idade} anos')

    print('\n')
    input("Precione qualquer tecla para sair...")