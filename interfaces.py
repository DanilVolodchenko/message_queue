import abc


class ICommand(abc.ABC):

    @abc.abstractmethod
    def execute(self) -> None:
        """Выполняет какое-то действие."""
