
def parse_seat(seat):
    if not isinstance(seat, str):
        return None

    seat = seat.strip()

    if len(seat) < 2:
        return None

    row = seat[0].upper()
    seat_number = seat[1:]

    if not row.isalpha() or not seat_number.isdigit():
        return None

    number = int(seat_number)

    if number <= 0:
        return None

    return row, number


def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        return None

    try:
        parts = prices_csv.split(',')

        if not parts or any(not p.strip() for p in parts):
            return None

        prices = [int(p.strip()) for p in parts]

        if any(price < 0 for price in prices):
            return None

        return round(sum(prices) * 1.18, 2)

    except ValueError:
        return None


def average_rating(ratings):
    if not isinstance(ratings, str):
        return None

    try:
        parts = ratings.split()

        if not parts:
            return None

        values = [int(r) for r in parts]

        if any(r < 1 or r > 5 for r in values):
            return None

        return round(sum(values) / len(values), 1)

    except ValueError:
        return None


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
