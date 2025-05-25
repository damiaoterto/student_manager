class Colorize:
    def __init__(self, text: str):
        self.text = text
        self.style = 0

    def bold(self):
        self.style = 1
        return self

    def red(self):
        return f'\033[{self.style};{31}{self.text}\033[0m'

    def yellow(self):
        return f'\033[{self.style};{33}{self.text}\033[0m'

    def cyan(self):
        return f'\033[{self.style};{36}{self.text}\033[0m'