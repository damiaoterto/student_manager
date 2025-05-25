from utils import clear_terminal, Colorize


class Menu:
    def __init__(self, title: str, description: str):
        self._title = title
        self._description = description
        self._items = []
        self._option = None

    def append_item(self, order: int, title: str, handler: callable):
        self._items.append({ 'order': order, 'title': title, 'handler': handler })

    def _mount_menu(self):
        while True:
            print(f'\n{self._title} - {self._description} \n')
            print(f'========================================')
            for item in self._items:
                print(f'[{item['order']}] - {item['title']}')
            print(f'========================================\n')

            try:
                self._option = int(input('Digite uma opção: '))
                selected_item = [item for item in self._items if item['order'] == self._option]
                clear_terminal()

                if not selected_item:
                    print(Colorize('\n Opção não encontrada, tente novamente. \n').bold().red())
                    input("\nPressione <enter> para continuar...")
                    continue

                selected_item[0]['handler']()
                clear_terminal()
            except ValueError:
                clear_terminal()
                print(Colorize('\nErro: Digite um número válido\n').bold().red())
                input("\nPressione <enter> para continuar...")
                clear_terminal()

    def show(self):
        self._mount_menu()


