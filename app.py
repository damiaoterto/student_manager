from infra import Database
from tui.context import Context
from tui.menu import Menu
import os

class Application:
    def __init__(self):
        self._context = Context(database=Database())

    def _mount_menu(self):
        menu = Menu('::Estudante', 'Menu de Operações')
        menu.append_item(1, 'Incluir', lambda: print('Opt 1'))
        menu.append_item(2, 'Listar', None)
        menu.append_item(3, 'Atualizar', None)
        menu.append_item(4, 'Excluir', None)
        menu.append_item(9, 'Sair', None)
        menu.show()

    def run(self):
        self._mount_menu()

    def exit(self):
        self._context.get_database().close()
        os._exit(0)