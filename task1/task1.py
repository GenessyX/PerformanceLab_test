import argparse

class RoundArray:
    def __init__(self, n: int):
        self.n: int = n
        self.num: int = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        return self.next()

    def next(self) -> int:
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
        else:
            cur, self.num = self.num, 1
        
        return cur


def solution(n: int, m: int) -> str:
    if m > n:
        m = m % n
        if m == 0:
            m = n

    round_array = RoundArray(n)
    cur = next(round_array)
    path = [cur]

    for _ in range(m-1):
        cur = next(round_array)
    
    if cur == 1:
        return "".join([str(x) for x in path])
    path.append(cur)

    while cur != 1:
        for _ in range(m-1):
            cur = next(round_array)
        if cur != 1:
            path.append(cur)

    return "".join([str(x) for x in path])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)
    args = parser.parse_args()
    n, m = args.n, args.m

    print(solution(n, m))

if __name__ == "__main__":
    main()
