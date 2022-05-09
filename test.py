from __future__ import annotations

class Test:
    def __init__(self, v:int) -> None:
        self.value = v
    
    def __add__(self, other:Type[self] ):
        return Test(self.value + other.value)

    def __str__(self) -> str:
        return str(self.value)

test1 = Test(5)
test2 = Test(7)

print(sum([test1, test2], Test(0)))
