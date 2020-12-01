# Find three numbers that sum to 2020, return their product


def txt_to_list(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines


def find_sum(input_list, target):
    input_list = list(map(int, input_list))
    for item1 in input_list:
        for item2 in input_list:
            intermediate = item1 + item2
            if target - intermediate in input_list:
                return item1, item2, target - intermediate
    return None, None, None


if __name__ == "__main__":
    input_list = txt_to_list("input.txt")
    first, second, third = find_sum(input_list, 2020)
    try:
        print(first, second, third, first * second * third)
    except TypeError:
        print("No triples sum to target")
