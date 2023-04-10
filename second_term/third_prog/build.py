import csv


def cut(length_prices: list) -> int:
    copy_prices = length_prices[:]
    for i in range(1, len(length_prices)):
        for j in range((i // 2) + 1):
            copy_prices[i] = max(copy_prices[i], copy_prices[i - j] + copy_prices[j])
    return copy_prices[len(length_prices) - 1]


def input_prices(length_prices: list) -> list:
    print('Write numbers one-by-one, write "exit" to quit')
    price = None
    while price != "exit":
        price = input()
        if price.isdigit() is True:
            length_prices.append(int(price))

    print(f'Prices were succsessfully added\n Modidied list: {length_prices}')
    return length_prices


def main() -> None:
    print('Do you want to write prices manually or from file?')
    print('1: file\n2: manually\n')
    action = int(input())
    if action == 1:
        length_prices = []
        with open('prices.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            lines = 0
            for row in csv_reader:
                if lines > 0 and row != []:
                    print(f'${row[0]} for {lines - 1} meters')
                    length_prices.append(int(row[0]))
                lines += 1

    else:
        length_prices = input_prices([0])

    print('Write length of the steel')
    steel_length = input()

    while steel_length.isdigit() is False:
        print('You can write only a number')
        steel_length = input()

    length_prices = length_prices[0:int(steel_length) + 1]

    optimal_price = cut(length_prices)

    print(f'Optimal price for {steel_length} meters of steel is ${optimal_price}')


if __name__ == '__main__':
    main()
