import csv
import time
from typing import Any


def input_file_path() -> str:
    """ input a path to .csv and check on validation """
    file_path: None = None
    print('Choose file')

    while file_path is None:
        file_path: str = str(input())

        try:
            with open(file_path, 'r'):
                pass
        except:
            print('Cannot open a file on this destination')
            file_path: None = None

    return file_path


def read_file_data(file_path: str) -> Any:
    """ parse to lists each el in text"""
    names: list = []
    volumes: list = []
    prices: list = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        lines: list = 0
        for row in csv_reader:
            if lines > 0 and row != []:
                names.append(row[0])
                volumes.append(int(row[1]))
                prices.append(int(row[2]))

            lines += 1

    return names, volumes, prices


def get_table_dynamic(volumes: list, prices: list, bag_volume: int) -> list:
    """
    make a table with prices per volume
    last column contains optimal (max) prices
    """
    volume: list = [[0 for x in range(bag_volume + 1)] for y in range(len(prices) + 1)]

    for x in range(len(prices) + 1):
        for y in range(bag_volume + 1):
            volume[x][y] = volume[x - 1][y]

            if x == 0 or y == 0:
                volume[x][y] = 0

            elif volumes[x - 1] <= y:
                volume[x][y] = max(prices[x - 1] + volume[x - 1][y - volumes[x - 1]], volume[x - 1][y])

    return volume


def get_table_recursion(volumes: list,
                        prices: list,
                        bag_volume: int,
                        items: int) -> list:
    """ trying to include/exclude item to find out best result """
    if items <= 0 or bag_volume <= 0:
        return 0
    # print(len(volumes), items, bag_volume)
    include = volumes[items] + get_table_recursion(volumes,
                                                   prices,
                                                   bag_volume - volumes[items],
                                                   items - 1)
    exclude = get_table_recursion(volumes, prices, bag_volume, items - 1)

    return max(include, exclude)


def get_optimal_prices_names(names: list,
                             volumes: list,
                             prices: list,
                             items: list) -> Any:
    """ convert lists with [volume, price] to item_name """
    named_items: list = []
    optimal_price: int = 0
    print(items)
    for i in range(len(names)):
        if [volumes[i], prices[i]] in items:
            named_items.append(names[i])
            optimal_price += prices[i]
            items.remove([volumes[i], prices[i]])

    return named_items, optimal_price


def greedy(names: list, volumes: list, prices: list, bag_volume: int) -> None:
    """ greddy picking items with max prices """
    taken_prices: list = []
    taken_volumes: list = []
    temp_prices = prices
    temp_volumes = volumes
    while bag_volume > 0:
        for _ in range(len(names)):
            item_position, price = find_biggest_price(names,
                                                      taken_prices,
                                                      temp_prices,
                                                      0,
                                                      0)
            if price != 0:
                bag_volume, taken_prices, taken_volumes = add_to_bad(bag_volume,
                                                                     taken_prices,
                                                                     taken_volumes,
                                                                     item_position)
                temp_prices, temp_volumes = remove_from_temp(temp_prices,
                                                             temp_volumes,
                                                             item_position)
            if bag_volume < 0:
                taken_prices.pop()
                taken_volumes.pop()
                break

    print_named_items(taken_prices)


def print_named_items(taken_prices: list) -> None:
    named_items: list = []
    for _ in range(len(taken_prices)):
        named_items.append(names[0])
        names.pop(0)
    print(f"""
           Items that give optimal price {named_items}
           optimal_price: ${sum(taken_prices)}
           """)


def add_to_bad(bag_volume: int,
               taken_prices: list,
               taken_volumes: list,
               item_position: int) -> tuple:

    bag_volume -= volumes[item_position]
    taken_prices.append(prices[item_position])
    taken_volumes.append(volumes[item_position])

    return bag_volume, taken_prices, taken_volumes


def remove_from_temp(temp_prices: list,
                     temp_volumes: list,
                     item_position: int) -> tuple:
    temp_prices.pop(item_position)
    temp_volumes.pop(item_position)

    return temp_prices, temp_volumes


def find_biggest_price(names: list,
                       taken_prices: list,
                       temp_prices: list,
                       price: int,
                       item_position: int) -> tuple:
    for i in range(len(names) - len(taken_prices)):
        if temp_prices[i] > price:
            item_position: int = i
            price: int = temp_prices[i]

    return item_position, price


def get_items(names: list,
              volumes: list,
              prices: list,
              volume: list,
              bag_volume: int) -> list:
    """
    by looking at the last column in the table, make a list
    subtract that from bag volume, to append the next item
    """

    res = volume[len(prices)][bag_volume]
    items: list = []

    for i in range(len(prices), 0, -1):
        if res <= 0:
            break

        if res == volume[i - 1][bag_volume]:
            continue

        else:
            items.append([volumes[i - 1], prices[i - 1]])
            res -= prices[i - 1]
            bag_volume -= volumes[i - 1]

    return items


def compare_speed(file_path: str,
                  mames: list,
                  volumes: list,
                  prices: list,
                  bag_volume: int,
                  named_prices: list,
                  named_items: list,
                  optimal_price: int) -> None:

    """ compare three method by time """
    elapsed_dynamic = time_dynamic(volumes, prices, bag_volume)
    elapsed_recursion = elapsed_dynamic * (2 ** len(named_items))
    elapsed_greedy = time_greddy(names, volumes, prices, bag_volume)
    print(f"""
           {round(elapsed_dynamic, 5)} seconds for dynamic
           {round(elapsed_recursion, 5)} seconds for recursion
           {round(elapsed_greedy, 10)} seconds for greedy
           """)


def time_dynamic(volumes: list,
                 prices: list,
                 bag_volume: int) -> Any:

    start = time.time()
    volume = get_table_dynamic(volumes, prices, int(bag_volume))
    items = get_items(names, volumes, prices, volume, int(bag_volume))
    named_items, optimal_price = get_optimal_prices_names(names,
                                                          volumes,
                                                          prices,
                                                          items)
    end = time.time()
    elapsed_dynamic = end - start

    return elapsed_dynamic


def time_greddy(names: list,
                volumes: list,
                prices: list,
                bag_volume: int) -> Any:
    start = time.time()
    greedy(names, volumes, prices, int(bag_volume))
    end = time.time()
    elapsed_greedy = end - start

    return elapsed_greedy


def main(file_path: str,
         names: list,
         volumes: list,
         prices: list,
         bag_volume: int,
         named_prices: list,
         named_items: list,
         optimal_price: int) -> str:

    table: str = """
            1: read a file
            2: write a bag volume
            3: solve the task
            4: check current items into bag
            5: write a path
            6: compare speed
            """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    action: str = input(table)

    while action.isdigit is False or (not (1 <= int(action) <= 9)):
        print(action_table if action != '-table' else table)
        action: str = input()

    if int(action) != 5 and file_path is None:
        print('Firstly read a file!')

    elif int(action) in (3, 4) and bag_volume is None:
        print('Write a bag volume firsty!')

    elif int(action) == 1:
        names, volumes, prices = read_file_data(file_path)

    elif int(action) == 2:
        bag_volume: str = input('Write a bag volume')

        while bag_volume.isdigit() is False:
            bag_volume: str = input('You can write only a number')

    elif int(action) == 3:
        method: int = int(input(
            """
            Choose method
            1: recursion
            2: dynamic
            3: greddy
            """))
        if method == 1:
            result = get_table_recursion(volumes,
                                         prices,
                                         int(bag_volume),
                                         len(volumes) - 1)
            print(result)
        if method == 2:
            volume = get_table_dynamic(volumes, prices, int(bag_volume))
            items = get_items(names, volumes, prices, volume, int(bag_volume))
            named_items, optimal_price = get_optimal_prices_names(names,
                                                                  volumes,
                                                                  prices,
                                                                  items)
            print(f"""
                   Items that give optimal price:\n{named_items}
                   optimal price is ${optimal_price}
                   """)

        if method == 3:
            greedy(names, volumes, prices, int(bag_volume))

    elif int(action) == 4 and named_items == []:
        print('Solve the taks firstly!')

    elif int(action) == 4:
        print(named_items)

    elif int(action) == 5:
        file_path = input_file_path()

    elif int(action) == 6:
        compare_speed(file_path,
                      names,
                      volumes,
                      prices,
                      bag_volume,
                      named_prices,
                      named_items,
                      optimal_price)

    return file_path, names, volumes, prices, bag_volume, named_prices, named_items, optimal_price


if __name__ == '__main__':
    file_path: str = None
    names: list = []
    volumes: list = []
    prices: list = []
    bag_volume: int = None
    named_items: list = []
    named_prices: list = []
    optimal_price: int = None

    while True:
        file_path, names, volumes, prices, bag_volume, named_prices, named_items, optimal_price = main(file_path,
                                                                                                       names,
                                                                                                       volumes,
                                                                                                       prices,
                                                                                                       bag_volume,
                                                                                                       named_prices,
                                                                                                       named_items,
                                                                                                       optimal_price)
