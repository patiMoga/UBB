from dataclasses import dataclass


@dataclass
class ClientAssemble:
    id: int
    name: str


@dataclass
class ClientFQAssemble:
    name: str
    freq: int


class ClientDTOAssemble:
    @staticmethod
    def create_client_dto(id, name):
        return ClientAssemble(id, name)

    @staticmethod
    def create_client_freq_dto(name, freq):
        return ClientFQAssemble(name, freq)