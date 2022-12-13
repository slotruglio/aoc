from functools import cmp_to_key

def compare(l,r):
  if type(l) == int and type(r) == int:
    if l<r: return -1
    return l>r
  if type(l) != int and type(r) != int:
    for i in range(min(len(l),len(r))):
      c = compare(l[i],r[i])
      if c: return c
    return compare(len(l),len(r))
  if type(l) == int and type(r) != int:
    return compare([l],r)
  if type(l) != int and type(r) == int:
    return compare(l,[r])

def day_13(input):
    signals = []
    correct_order_sum = 0
    with open(input, "r") as f:
        to_match = None
        pair_counter = 1
        for line in f.readlines():
            if line == "\n":
                continue
            line = line.strip()
            if to_match is None:
                to_match = (eval(line), pair_counter)
                pair_counter += 1
                continue

            # if to_match is not None:
            first, pair_index = to_match
            second = eval(line)

            if compare(first,second)<=0:
                correct_order_sum += pair_index
            signals.extend([first, second])
            to_match = None

    d1, d2 = [[2]], [[6]]
    signals.extend([d1, d2])
    signals.sort(key=cmp_to_key(compare))
    return (correct_order_sum, (signals.index(d1)+1)*(signals.index(d2)+1))

if __name__ == '__main__':
    one,two = day_13("2022/inputs/day13/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)