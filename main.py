from tui import Menu
import os

def main():
    try:
        menu = Menu('::Estudante', 'Menu de Operações')

        menu.append_item('Incluir', None)
        menu.append_item('Listar', None)
        menu.append_item('Atualizar', None)
        menu.append_item('Excluir', None)
        menu.append_item('Sair', None)

        menu.show()
    except KeyboardInterrupt:
        os._exit(0)

if __name__ == '__main__':
    main()