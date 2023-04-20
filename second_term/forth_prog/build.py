import csv
from typing import Any


def input_file_path() -> str:
    file_path = None
    print('Choose file')

    while file_path is None:
        file_path = str(input())

        try:
            with open(file_path, 'r'):
                pass
        except:
            print('Cannot open a file on this destination')
            file_path = None

    return file_path


def read_file_data(file_path: str) -> Any:
    names = []
    volumes = []
    prices = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        lines = 0
        for row in csv_reader:
            if lines > 0 and row != []:
                names.append(row[0])
                volumes.append(int(row[1]))
                prices.append(int(row[2]))

            lines += 1

    return names, volumes, prices


def get_table(volumes: list, prices: list, bag_volume: int) -> list:
    volume = [[0 for x in range(bag_volume + 1)] for y in range(len(prices) + 1)]

    for x in range(len(prices) + 1):
        for y in range(bag_volume + 1):
            if x == 0 or y == 0:
                volume[x][y] = 0

            elif volumes[x - 1] <= y:
                volume[x][y] = max(prices[x - 1] + volume[x - 1][y - volumes[x - 1]],
                                   volume[x - 1][y])

            else:
                volume[x][y] = volume[x - 1][y]

    return volume


def get_optimal_prices_names(names: list,
                             volumes: list,
                             prices: list,
                             items: list) -> Any:
    named_items = []
    optimal_price = 0
    print(items)
    for i in range(len(names)):
        if [volumes[i], prices[i]] in items:
            named_items.append(names[i])
            optimal_price += prices[i]
            items.remove([volumes[i], prices[i]])

    return named_items, optimal_price


def get_items(names: list,
              volumes: list,
              prices: list,
              volume: list,
              bag_volume: int) -> list:

    res = volume[len(prices)][bag_volume]
    items = []

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


def main() -> None:
    file_path = input_file_path()
    names, volumes, prices = read_file_data(file_path)

    print('Write a bag volume')
    bag_volume = input()
    while bag_volume.isdigit() is False:
        print('You can write only a number')
        bag_volume = input()

    volume = get_table(volumes, prices, int(bag_volume))
    items = get_items(names, volumes, prices, volume, int(bag_volume))
    named_items, optimal_price = get_optimal_prices_names(names,
                                                          volumes,
                                                          prices,
                                                          items)

    print(named_items, optimal_price)


if __name__ == '__main__':
    main()
