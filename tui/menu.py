class Menu:
    def __init__(self, title: str, description: str):
        self._title = title
        self._description = description
        self._items = []
        self._option = None

    def append_item(self, title: str, handler: callable):
        self._items.append({ 'title': title, 'handler': handler })

    def show(self):
        item_idx = 1
        print(f'\n{self._title} - {self._description} \n')
        print(f'========================================')
        for item in self._items:
            print(f'[{item_idx}] - {item['title']}')
            item_idx += 1
        print(f'========================================\n')
        self._option = int(input('Digite uma opção: '))


