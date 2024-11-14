from dataclasses import dataclass, asdict
import json


def to_snake_camel(d: dict):
    for k in d.copy().keys():
        words = [w.capitalize() for w in k.split("_")]
        words[0] = words[0].lower()
        if isinstance(d[k], (str, int)):
            if len(words) > 1:
                ck = "".join(words)
                d[ck] = d[k]
                d.pop(k)
        elif isinstance(d[k], list):
            if len(words) > 1:
                ck = "".join(words)
            else:
                ck = k
            d[ck] = []
            for elm in d[k]:
                if isinstance(elm, dict):
                    d[ck].append(to_snake_camel(elm))
                else:
                    d[ck].append(elm)
            d.pop(k)
        elif isinstance(d[k], dict):
            if len(words) > 1:
                ck = "".join(words)
            else:
                ck = k
            d[ck] = to_snake_camel(d[k])
            d.pop(k)
    return d


@dataclass
class NestNestClass():
    number: int
    fugafuga_name: str


@dataclass
class NestClass():
    number: int
    fuga_name: str
    nestnest_class: NestNestClass


@dataclass
class CamelClass():
    name: str
    hoge_revision: int
    hoge_list: list[NestClass]


c = CamelClass("aaa", 3, [NestClass(3, "foo", NestNestClass(2, "bar"))])
tc = to_snake_camel(asdict(c))
print(json.dumps(asdict(c)))
print(json.dumps(tc))
