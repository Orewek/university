import csv


class City_17(object):
    """ a class with some methods and arguments """
    def __init__(self, ppl: int, mayor: str, age: int, name: str) -> None:
        self.population = ppl
        self.mayor = mayor
        self.age = age
        self.name = name

    def greetings(self) -> str:
        return (f'Welcome to {self.name}!')

    def mayor_election(self) -> str:
        return (f'{self.mayor} won')

    def say_population(self) -> str:
        return (f'{self.population}, ppl r living in {self.name} rn')


def add_city(cities: list) -> list:
    """ add a new city with some properties to list of cities """
    print('Write a name of city')
    name = str(input())

    print('How many ppl r living in this city')
    population = input()
    while population.isdigit() is False:
        print('You can write only digits in population category')
        population = input()

    print('Whos the mayor of that city')
    mayor = str(input())

    print('How many years this city exist')
    age = input()

    while age.isdigit() is False:
        print('You can write only digits in age category')
        age = input()

    city_name = City_17(int(population), mayor, int(age), name.capitalize())
    cities.append(city_name)
    print(f'{city_name.name} was succsessfully added')

    return cities


def delete_city(cities: list) -> list:
    """ delete a city from the list """
    for count, city in enumerate(cities):
        print(count + 1, city.name)

    print('Write a number next to the city which we should delete')

    action = input()

    while action.isdigit is False or (not (1 <= int(action) <= len(cities))):
        print('You can write only a number or number <= 0 / >= last city')
        action = input()

    del cities[int(action) - 1]

    print('City was succsessfully deleted')

    return cities


def action_menu(action_city: str, city: City_17, new_info: str) -> None:
    """ change some atribute in city """
    if int(action_city) == 1:
        city.name = new_info

    if int(action_city) == 2:
        city.age = int(new_info)

    if int(action_city) == 3:
        city.population = int(new_info)

    if int(action_city) == 4:
        city.mayor = new_info


def change_smth_city(cities: list) -> list:
    """ change some information for city into the list """
    for count, city in enumerate(cities):
        print(count + 1, city.name)

    print('Choose in which city we should change info')

    action = input()

    while action.isdigit is False or (not (1 <= int(action) <= len(cities))):
        print('You can write only a number or number <= 0 / >= last city')
        action = input()

    city = cities[int(action) - 1]

    print('Choose what exactly should we change in this city')

    table = """
            1: name
            2: age
            3: population
            4: mayor
            """

    print(table)

    action_city = input()

    while action_city.isdigit is False or (not (1 <= int(action_city) <= 4)):
        print('You can write only a number or number <= 0 / > 4')
        action_city = input()

    print('Write updated info')

    new_info = input()

    while (2 <= int(action_city) <= 3) and new_info.isdigit() is False:
        print('You can write only digits to age and population')
        new_info = input()

    action_menu(action_city, city, new_info)

    return cities


def show_city_info(cities: list) -> list:
    """ show properties of exact city """
    for count, city in enumerate(cities):
        print(count + 1, city.name)

    print('Write number next to city, to see info about')

    action = input()

    while action.isdigit() is False or (not (1 <= int(action) <= len(cities))):
        print('You can write only a number or number <= 0 / >= last city')
        action = input()

    city = cities[int(action) - 1]
    print(f'name: {city.name}\n'
          f'population: {city.population}\n'
          f'age: {city.age}\n'
          f'mayor: {city.mayor}\n')

    return cities


def cities_satisty_filter(action_city: str, less_big: str, border: str) -> None:
    """ print cities that satisfy the filter """
    if int(action_city) == 2 and int(less_big) == 1:
            for city in cities:
                if city.age < int(border):
                    print(city.name, city.age)

    if int(action_city) == 2 and int(less_big) == 2:
            for city in cities:
                if city.age > int(border):
                    print(city.name, city.age)

    if int(action_city) == 3 and int(less_big) == 1:
        for city in cities:
            if city.population < int(border):
                print(city.name, city.population)

    if int(action_city) == 3 and int(less_big) == 2:
        for city in cities:
            if city.population > int(border):
                print(city.name, city.population)


def city_filter(cities: list) -> list:
    """ ouput all cities that satisfy the filter """
    print('Choose which parameter should we use')

    table = """
            1: name
            2: age
            3: population
            4: mayor
            """

    print(table)

    action_city = input()

    while action_city.isdigit() is False or (not (2 <= int(action_city) <= 3)):
        print('You can make age/population filter')
        action_city = input()

    print('less 1; bigger 2')
    less_big = input()
    while less_big.isdigit() is False or (not (1 <= int(less_big) <= 2)):
        print('You can write only 1 or 2')
        less_big = input()

    print('Write number, with that we will compare rest')
    border = input()

    while border.isdigit() is False:
        print('You can write only a number')
        border = input()

    cities_satisty_filter(action_city, less_big, border)

    return cities


def show_all_cities_info(cities: list) -> list:
    """ show all cities from the list and their properties """
    for city in cities:
        print(f'name: {city.name}\n'
              f'population: {city.population}\n'
              f'age: {city.age}\n'
              f'mayor: {city.mayor}\n')

    return cities


def city_counter(cities: list) -> list:
    """ show how many cities currently in the list """
    print(f'Have {len(cities)} cities in our list')

    return cities


def main_menu(cities: list, action: int) -> list:
    switcher = {
        1: add_city,
        2: delete_city,
        3: change_smth_city,
        4: show_city_info,
        5: city_filter,
        6: show_all_cities_info,
        7: city_counter,
    }
    cities = switcher[action](cities)

    return cities


def main(cities: list) -> list:

    table = """
            1: add city
            2: delete city
            3: change smth in city
            4: show city info
            5: city filter
            6: show all cities info
            7: city counter
            8: exit
            """

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    print(table)

    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while action.isdigit() is False or (not (0 < int(action) < 9)):
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action = input()

    if int(action) == 8:
        exit()
    cities = main_menu(cities, int(action))

    return cities


if __name__ == '__main__':
    cities = []
    file_path = None
    print('Choose the file')
    while file_path is None:
        file_path = str(input())

        try:
            with open(file_path, 'r'):
                pass

        except:
            print('cannot open file on this destination')
            file_path = None

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        lines = 0
        for row in csv_reader:
            if lines > 0 and row != []:
                city_name = City_17(int(row[0]), row[1], int(row[2]), row[3])
                cities.append(city_name)

            lines += 1
    for city in cities:
        print(city.name)
    while True:
        cities = main(cities)
        with open('new_file.csv', mode='w') as csv_file:
            fieldnames = ['population', 'mayor', 'age', 'name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            for city in cities:
                writer.writerow({'population': f'{city.population}',
                                'mayor': f'{city.mayor}',
                                'age': f'{city.age}',
                                'name': f'{city.name}'})
