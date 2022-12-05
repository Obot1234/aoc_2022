from typing import TypeVar

T = TypeVar('T')


def batched(_list: list[T], n: int) -> list[list[T]]:
    for k in range(0, len(_list), n):
        if k + n <= len(_list):
            yield _list[k:(k + n)]
