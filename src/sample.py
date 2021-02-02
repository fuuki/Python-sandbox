from dataclasses import dataclass, field
from typing import List
import random


@dataclass
class Board:
    """
    Cell index image (width = 3)
        x 0 1 2
    y   +-------
    0   | 0 1 2
    1   | 3 4 5
    2   | 6 7 8
    """

    hits: List[int] = field(default_factory=list)
    width: int = 3

    def hit(self, x: int, y: int):
        cell = x + y * self.width
        self.hits.append(cell)

    def hit_direct(self, cell: int):
        self.hits.append(cell)

    def is_hit(self, x: int, y: int) -> bool:
        cell = x + y * self.width
        return cell in self.hits

    def count_bingo(self) -> int:
        result = 0
        # 縦
        for x in range(self.width):
            for y in range(self.width):
                if not self.is_hit(x, y):
                    break
            else:
                result += 1
        # 横
        for y in range(self.width):
            for x in range(self.width):
                if not self.is_hit(x, y):
                    break
            else:
                result += 1
        # 斜め
        for i in range(self.width):
            if not self.is_hit(i, i):
                break
        else:
            result += 1
        for i in range(self.width):
            if not self.is_hit(i, self.width-i):
                break
        else:
            result += 1
        return result

def main():
    test_count = 100000
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(test_count):
        res = experiment_2()
        result[res] += 1
        if i % 10000 == 0:
            print(".")
    print(result)

def experiment_1() -> int:
    # 初めてビンゴになったとき
    board = Board()
    drawOrder = list(range(9))
    random.shuffle(drawOrder)
    for d in drawOrder:
        board.hit_direct(d)
        if (c := board.count_bingo()) > 0:
            return c
    return 0

def experiment_2() -> int:
    # 特定個数埋めたとき
    cap = 7
    board = Board()
    drawOrder = list(range(9))
    random.shuffle(drawOrder)
    for d in drawOrder[:cap]:
        board.hit_direct(d)
    return board.count_bingo()

if __name__ == '__main__':
    main()