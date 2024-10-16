import dataclasses
from fuga.fuga import Fuga
from hoge.hoge import Product, ProductInfo
from log import logger


@dataclasses.dataclass
class MainProduct:
    main: str


f = Fuga(Product("hog", 3, [ProductInfo("foo")]))
print(f)

logger.debug("hello debug")
logger.info("hello info")
logger.warning("hello warning")
logger.error("hello error")


def print_error(msg: str):
    COLOR_RED = "\033[31m"
    COLOR_RESET = "\033[0m"

    print(COLOR_RED + f"{msg}" + COLOR_RESET)


print("helloworld")
print_error(f)
