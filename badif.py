

from typing import Callable


class _If:
    def __init__(self, cond: bool) -> None:
        self._done = cond

    def Elif(self, cond):
        def wrapper(func: Callable):
            done = self._done
            done or ((done := cond) and func())
            self._done = done
            return self
        return wrapper

    def Else(self, func: Callable):
        self._done or func()
        self._done == True
        del self


def If(cond):
    def wrapper(func: Callable):
        cond and func()
        return _If(bool(cond))
    return wrapper

