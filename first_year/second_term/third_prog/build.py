import csv
from typing import Any


def check_int(int_variable: Any) -> int:
    while int_variable.isdigit() is False:
        int_variable: str = input('You can write only digits')

    return int_variable


def cut(length_prices: list) -> Any:
    prices_per_meter: list = []
    prices: list = length_prices[:]
    list_indexes: list = []
    for i in range(1, len(length_prices)):
        current_price = 0
        for j in range((i // 2) + 1):
            prices[i]: int = max(prices[i], prices[i - j] + prices[j])
            if (prices[i] > current_price):
                current_price = prices[i]
                indexes = [i - j, j]

        prices_per_meter.append(prices[i])
        list_indexes.append(indexes)

    return prices_per_meter, list_indexes


def make_total_list(meters_list: list, prices_list: list) -> list:
    total_list: list = []
    prices_list: list = prices_list[1:]
    print(f"""
           meters list: {meters_list}
           prices list: {prices_list}
           """)

    for i in range(int(meters_list[-1]) + 1):
        if i not in meters_list:
            total_list.append(0)
        else:
            total_list.append(prices_list[0])
            prices_list: list = prices_list[1:]

    return total_list


def input_prices(length_prices: list) -> list:
    print('Write numbers one-by-one, write "exit" to quit')
    price: str = ''
    meters: str = ''
    meters_list: list = []
    while price.lower() != "exit" and meters.lower() != "exit":
        meters: int = input('Write a  meter')

        if meters != "exit":
            price: int = input(f'Write a price for {meters} meters')

        if price.isdigit() is True and meters.isdigit() is True and int(meters) not in meters_list:
            length_prices.append(int(price))
            meters_list.append(int(meters))

        elif price.lower() != "exit" and meters.lower() != "exit":
            print('You can write only numbers as a price or meter')

    print(f"""
           Prices were succsessfully added
           Modidied pricee list: {length_prices[1:]}
           meters list: {meters_list}
           """)

    length_prices: list = make_total_list(meters_list, length_prices)
    return length_prices


def read_info_from_file(length_prices: list) -> list:
    with open('prices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lines: int = 0
        meters_list: list = []

        for row in csv_reader:
            if lines > 0 and row != []:
                length_prices.append(int(row[1]))
                meters_list.append(int(row[0]))
            lines += 1

    length_prices: list = make_total_list(meters_list, length_prices)
    return length_prices


def make_correct_length(meters: int, list_indexes: list) -> list:
    new_list: list = []
    if list_indexes[meters - 1][0] != meters:
        print(meters, list_indexes[meters - 1])
        new_list.append(list_indexes[meters - 1][0])
        new_list.append(list_indexes[meters - 1][1])

    for _ in range(3):
        for i in range(len(new_list)):
            meters: int = new_list[i]
            if list_indexes[meters - 1][0] != meters:
                print(meters, list_indexes[meters - 1])
                new_list.append(list_indexes[meters - 1][0])
                new_list.append(list_indexes[meters - 1][1])
                new_list.pop(i)

    total_list: list = [0] * 10
    for i in new_list:
        total_list[i - 1] += 1

    if total_list == [0] * 10:
        total_list[meters - 1] += 1

    print(total_list)
    return total_list


def main() -> None:
    print("""
          Do you want to write prices manually or from file?
          1: file\n2: manually
          """)

    action: int = input()
    while action.isdigit() is False or (int(action) != 1 and int(action) != 2):
        action: int = input('You can write only 1 or 2')

    if int(action) == 1:
        length_prices: int = read_info_from_file([0])
    else:
        length_prices: int = input_prices([0])

    steel_length: int = input('Write length of the steel')

    while steel_length.isdigit() is False:
        steel_length: int = input('You can write only a number')

    length_prices: list = length_prices[0:int(steel_length) + 1]

    optimal_prices, list_indexes = cut(length_prices)
    print(list_indexes)

    if int(steel_length) > (len(length_prices) - 1):
        total_price: int = 0
        for i in range(len(optimal_prices)):
            parts: int = int(steel_length) // (i + 1)
            free_metrs: int = int(steel_length) % (i + 1)

            if free_metrs != 0:
                new_price: int = parts * optimal_prices[i] + optimal_prices[free_metrs - 1]
            else:
                new_price: int = parts * optimal_prices[i]

            main_shard: int = i + 1
            total_price: int = max(total_price, new_price)

        total_list: list = make_correct_length(main_shard, list_indexes)
        for i in range(10):
            total_list[i] *= parts

        shard_total_list: list = make_correct_length(free_metrs, list_indexes)
        for i in range(10):
            total_list[i] += shard_total_list[i]
        print(total_list)

    else:
        total_list: list = make_correct_length(int(steel_length), list_indexes)
        total_price: int = optimal_prices[int(steel_length) - 1]

    text: str = ''
    for i in range(10):
        if total_list[i] != 0:
            if text != '':
                text += ' and '
            text += f'{i + 1}x{total_list[i]}'

    print(f'{text} for ${total_price}')


if __name__ == '__main__':
    main()
