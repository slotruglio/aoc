from ast import literal_eval

def compare_array(first, sec, level=0):
    second = [sec] if isinstance(sec, int) else sec
    level_str = "-"*level
    print(f"{level_str}- Compare: {first} vs {second}")
    if level == 0 and len(first) > len(second):
        return False
    for i in range(len(first)):
        if not isinstance(first[i], int):
            try:
                if not compare_array(first[i], second[i], level+1):
                    return False
            except IndexError:
                return False
        elif isinstance(first[i], int) and not isinstance(second[i], int):
            this_left = [first[i]]
            try:
                if not compare_array(this_left, second[i], level+1):
                    return False
            except IndexError:
                return False
        else:
            #print(f"Compare: {first[i]} vs {sec[0]}")
            try:
                print(f"-{level_str}- Compare: {first[i]} vs {second[i]}")
                if first[i] > second[i]:
                    return False
                if first[i] < second[i]:
                    return True
            except IndexError:
                continue
            except:
                return False
    return True

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
    correct_order_sum = 0
    with open(input, "r") as f:
        to_match = None
        pair_counter = 1
        for line in f.readlines():
            if line == "\n":
                continue
            line = line.strip()
            if to_match is None:
                to_match = (literal_eval(line), pair_counter)
                pair_counter += 1
                continue

            # if to_match is not None:
            first, pair_index = to_match
            second = literal_eval(line)

            if compare(first,second)<=0: correct_order_sum += pair_index
            to_match = None


    return (correct_order_sum,0)

if __name__ == '__main__':
    one,two = day_13("2022/inputs/day13/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)