class Colorize:
    def __init__(self, text: str):
        self.text = text
        self.style = 0

    def bold(self):
        self.style = 1
        return self

    def red(self, bg=40):
        return f"\033[{self.style};{31};{bg}m{self.text}\033[0m"

    def yellow(self, bg=40):
        return f"\033[{self.style};{33};{bg}m{self.text}\033[0m"

    def cyan(self, bg=40):
        return f"\033[{self.style};{36};{bg}m{self.text}\033[0m"