import dataclasses


@dataclasses.dataclass
class ProductInfo:
    msg: str


@dataclasses.dataclass
class Product:
    name: str
    rev: int
    msgs: list[ProductInfo]
