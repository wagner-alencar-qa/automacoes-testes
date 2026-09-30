class AbstractTransaction:
    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

    def do(self, *args, **kwargs):
        raise NotImplementedError("Transaction deve implementar o método do().")
