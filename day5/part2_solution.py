# What is the highest ID on a boarding pass


def txt_to_list(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines


def get_seat(seat_string, plane_dim):
    seats = [i for i in range(plane_dim)]
    for letter in seat_string:
        divider = len(seats) // 2
        if letter in ["F", "L"]:
            seats = seats[:divider]
        else:
            seats = seats[divider:]
    return seats[0]


def get_seat_id(seat_string):
    return get_seat(seat_string[:7], 128) * 8 + get_seat(seat_string[7:], 8)


def generate_all_seat_ids(rows, columns):
    ids = []
    for row in range(rows):
        for column in range(columns):
            ids.append(row * 8 + column)
    return ids


def has_neighbor(seat_ids, ticketed):
    return [seat for seat in seat_ids if seat - 1 in ticketed and seat + 1 in ticketed]


if __name__ == "__main__":
    seats = txt_to_list("input.txt")
    all = generate_all_seat_ids(128, 8)
    ticketed = [get_seat_id(seat) for seat in seats]
    remainder = [i for i in all if i not in ticketed]
    my_seat = has_neighbor(remainder, ticketed)
    print(my_seat)
