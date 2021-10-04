# -*- coding: UTF-8 -*-

class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        print("get x")
        return self._x

    @x.setter
    def x(self, x):
        print("set x")
        self._x = x

    @property
    def y(self):
        print("get y")
        return self._y

    @y.setter
    def y(self, y):
        print("set y")
        self._y = y


if __name__ == '__main__':
    p = Point(1, 2)
    print(f"x:{p.x}, y:{p.y}")
    p.x = 10
    p.y = 20
    print(f"x:{p.x}, y:{p.y}")
