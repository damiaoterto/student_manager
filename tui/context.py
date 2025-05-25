class Context:
    def __init__(self, database):
        self._database = database

    def get_database(self):
        return self._database