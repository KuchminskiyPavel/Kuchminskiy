from abc import ABC, abstractmethod


class Chess_figure(ABC):
    def __init__(self, x: int, y: int, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def attack(self, x, y) -> bool:
        pass


class Queen(Chess_figure):
    def attack(self, x, y) -> bool:
        if (self.x - x == 0) or (self.y - y == 0) or abs(self.x - x) == abs(self.y - y):
            return True
        else:
            return False


class Pawn(Chess_figure):
    def attack(self, x, y) -> bool:
        if self.color == 'Белый':
            if self.x - x == 1 and abs(self.y - y) == 1:
                return True
        elif self.color == 'Черный':
            if self.x - x == 1 and abs(self.y - y) == 1:
                return True
        return False


class Knight(Chess_figure):
    def attack(self, x, y) -> bool:
        x1 = abs(self.x - x)
        y1 = abs(self.y - y)
        if (x1 == 1 and y1 == 2) or (x1 == 2 and y1 == 1):
            return True
        return False


queen = Queen(4, 4, 'Белый')
pawn = Pawn(6, 6, 'Черный')
knight = Knight(2, 3, 'Белый')

print(queen.attack(6, 4))
print(pawn.attack(5, 5))
print(knight.attack(4, 5))


