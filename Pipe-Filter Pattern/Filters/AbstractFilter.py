from abc import abstractmethod
from Invoice import Invoice
class AbstractFilter:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, invoice: Invoice) -> Invoice:
        return Invoice
