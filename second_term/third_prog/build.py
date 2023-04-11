import csv


def cut(length_prices: list) -> int:
    prices = length_prices[:]
    for i in range(1, len(length_prices)):
        for j in range((i // 2) + 1):
            prices[i] = max(prices[i], prices[i - j] + prices[j])
    return prices[len(length_prices) - 1]


def input_prices(length_prices: list) -> list:
    print('Write numbers one-by-one, write "exit" to quit')
    price = ''
    meters = ''
    included_list = []
    while price.lower() != "exit" and meters.lower() != "exit":
        print('Write a  meter')
        meters = input()

        if meters != "exit":
            print(f'Write a price for {meters} meters')
            price = input()

        if price.isdigit() is True and meters.isdigit() is True and int(meters) not in included_list:
            length_prices.append(int(price))
            included_list.append(int(meters))

        elif price.lower() != "exit" and meters.lower() != "exit":
            print('You can write only numbers as a price or meter')

    print(f'Prices were succsessfully added\n'
          f'Modidied pricee list: {length_prices[1:]}\n'
          f'meters list: {included_list}')
    return length_prices


def read_info_from_file(length_prices: list) -> list:
    with open('prices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lines = 0
        for row in csv_reader:
            if lines > 0 and row != []:
                print(f'${row[0]} for {lines} meters')
                length_prices.append(int(row[0]))
            lines += 1

    return length_prices


def main() -> None:
    print('Do you want to write prices manually or from file?')
    print('1: file\n2: manually\n')

    action = input()
    while action.isdigit() is False or (int(action) != 1 and int(action) != 2):
        print('You can write only 1 or 2')
        action = input()

    if int(action) == 1:
        length_prices = read_info_from_file([0])
    else:
        length_prices = input_prices([0])

    print('Write length of the steel')
    steel_length = input()

    while steel_length.isdigit() is False:
        print('You can write only a number')
        steel_length = input()

    length_prices = length_prices[0:int(steel_length) + 1]

    optimal_price = cut(length_prices)

    print(f'Optimal price for {steel_length} meters is ${optimal_price}')


if __name__ == '__main__':
    main()
