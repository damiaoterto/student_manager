from handlers import insert_handler, list_handler, delete_handler
from handlers.update_handler import update_handler
from infra import Database
from tui.context import Context
from tui.menu import Menu
import os

class Application:
    def __init__(self):
        self._context = Context(database=Database())

    def _mount_menu(self):
        menu = Menu('::Estudante', 'Menu de Operações')
        menu.append_item(1, 'Incluir', lambda: insert_handler(self._context))
        menu.append_item(2, 'Listar', lambda: list_handler(self._context))
        menu.append_item(3, 'Atualizar', lambda: update_handler(self._context))
        menu.append_item(4, 'Excluir', lambda: delete_handler(self._context))
        menu.append_item(9, 'Sair', lambda: self.exit())
        menu.show()

    def run(self):
        self._mount_menu()

    def exit(self):
        self._context.get_database().close()
        os._exit(0)