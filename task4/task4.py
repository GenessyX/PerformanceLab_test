import argparse
import os

def median(l: list) -> float:
    l = sorted(l)
    n = len(l)
    if n % 2 == 0:
        m = (l[n//2] + l[n//2 - 1])/2
    else:
        m = l[n//2]
    return m

def minimal_steps(l: list) -> int:
    med = round(median(l))

    return int(sum([abs(x - med) for x in l]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('values_file', type=str)
    args = parser.parse_args()

    values_file = args.values_file

    if (not os.path.exists(values_file)):
        raise Exception("File not found")

    with open(values_file, 'r') as v_f:
        values = [int(x.strip()) for x in v_f.readlines()]

    print(minimal_steps(values))
    
    

if __name__ == "__main__":
    main()