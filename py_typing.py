# -*- coding: UTF-8 -*-
from typing import Dict, List, Tuple, Sequence, NewType, TypeVar


def greeting(name: str) -> str:
    # basic typing
    return f'Hello {name}'


Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    print(message, servers)
    pass


T = TypeVar('T')  # Declare type variable


def first(l: Sequence[T]) -> T:  # Generic function
    return l[0]


class Base:
    pass


class Child(Base):
    pass


def func(x: Base) -> None:
    pass


if __name__ == '__main__':
    # variable with type
    name: str = "Trump"
    print(greeting(name))
    # type checks; a list of floats qualifies as a Vector.
    print(scale(2.0, [1.0, -4.2, 5.4]))

    # new type
    UserId = NewType('UserId', int)
    some_id = UserId(524313)
    print(f"some_id = {some_id}")
    print(first([1, 2, 3, 4, 5]))
    func(Child())
