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
    correct_order_sum = 0   # part 1
    d1, d2 = [[2]], [[6]]   # part 2
    signals = [d1, d2]      # part 2
    with open(input, "r") as f:
        for i,s in enumerate(f.read().split("\n\n")):
            left, right = [eval(x) for x in s.split()]

            if compare(left,right)<=0: correct_order_sum += i+1 # part 1
            signals.extend([left, right])                       # part 2

    signals.sort(key=cmp_to_key(compare))

    return (correct_order_sum, (signals.index(d1)+1)*(signals.index(d2)+1))

if __name__ == '__main__':
    one,two = day_13("2022/inputs/day13/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)