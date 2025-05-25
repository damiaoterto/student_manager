from tui import Menu
import os

def main():
    try:
        menu = Menu('::Estudante', 'Menu de Operações')
        menu.append_item(1, 'Incluir', lambda: print('Opt 1'))
        menu.append_item(2, 'Listar', None)
        menu.append_item(3, 'Atualizar', None)
        menu.append_item(4, 'Excluir', None)
        menu.append_item(9, 'Sair', None)
        menu.show()
    except KeyboardInterrupt:
        os._exit(0)

if __name__ == '__main__':
    main()