import csv


class City_17(object):
    """ a class with some methods and arguments """
    def __init__(self, ppl: int, mayor: str, age: int, name: str) -> None:
        self.population: int = ppl
        self.mayor: str = mayor
        self.age: int = age
        self.name: str = name

    def greetings(self) -> str:
        return (f'Welcome to {self.name}!')

    def mayor_election(self) -> str:
        return (f'{self.mayor} won')

    def say_population(self) -> str:
        return (f'{self.population}, ppl r living in {self.name} rn')


def add_city(cities: list) -> list:
    """ add a new city with some properties to list of cities """
    name: str = str(input('Write a name of city'))

    population: int = input('How many ppl r living in this city')
    while population.isdigit() is False:
        population: int = input('You can write only digits in population category')

    mayor: str = str(input('Whos the mayor of that city'))
    age: int = input('How many years this city exist')

    while age.isdigit() is False:
        age: str = input('You can write only digits in age category')

    city_name: str = City_17(int(population), mayor, int(age), name.capitalize())
    cities.append(city_name)
    print(f'{city_name.name} was succsessfully added')

    return cities


def delete_city(cities: list) -> list:
    """ delete a city from the list """
    print(*[f'{count + 1} {city.name}' for count, city in enumerate(cities)], sep='\n')

    action: int = input('Write a number next to the city which we should delete')

    while action.isdigit is False or (not (1 <= int(action) <= len(cities))):
        action: int = input('You can write only a number or number <= 0 / >= last city')

    del cities[int(action) - 1]

    print('City was succsessfully deleted')

    return cities


def action_menu(action_city: str, city: City_17, new_info: str) -> None:
    """ change some atribute in city """
    if int(action_city) == 1:
        city.name: str = new_info

    if int(action_city) == 2:
        city.age: int = int(new_info)

    if int(action_city) == 3:
        city.population: int = int(new_info)

    if int(action_city) == 4:
        city.mayor: str = new_info


def change_smth_city(cities: list) -> list:
    """ change some information for city into the list """

    print(*[f'{count + 1} {city.name}' for count, city in enumerate(cities)], sep='\n')

    action: int = input('Choose in which city we should change info')

    while action.isdigit is False or (not (1 <= int(action) <= len(cities))):
        action: int = input('You can write only a number or number <= 0 / >= last city')

    city: str = cities[int(action) - 1]

    print('Choose what exactly should we change in this city')

    table: str = """
            1: name
            2: age
            3: population
            4: mayor
            """

    action_city: int = input(table)

    while action_city.isdigit is False or (not (1 <= int(action_city) <= 4)):
        action_city: int = input('You can write only a number or number <= 0 / > 4')

    new_info: int = input('Write updated info')

    while (2 <= int(action_city) <= 3) and new_info.isdigit() is False:
        new_info: int = input('You can write only digits to age and population')

    action_menu(action_city, city, new_info)

    return cities


def show_city_info(cities: list) -> list:
    """ show properties of exact city """
    print(*[f'{count + 1} {city.name}' for count, city in enumerate(cities)], sep='\n')

    action: int = input('Write number next to city, to see info about')

    while action.isdigit() is False or (not (1 <= int(action) <= len(cities))):
        action = input('You can write only a number or number <= 0 / >= last city')

    city: str = cities[int(action) - 1]
    print(f"""
           name: {city.name}
           population: {city.population}
           age: {city.age}
           mayor: {city.mayor}
           """)

    return cities


def cities_satisty_filter(action_city: int, less_big: int, border: int) -> None:
    """ print cities that satisfy the filter """
    if action_city == 2 and less_big == 1:
        print(*[[city.name, city.age] for city in cities if city.age < border])

    if action_city == 2 and less_big == 2:
        print(*[[city.name, city.age] for city in cities if city.age > border])

    if action_city == 3 and less_big == 1:
        print(*[[city.name, city.population] for city in cities if city.age < border])

    if action_city == 3 and less_big == 2:
        print(*[[city.name, city.population] for city in cities if city.age > border])


def city_filter(cities: list) -> list:
    """ ouput all cities that satisfy the filter """
    print('Choose which parameter should we use')

    table: str = """
            1: name
            2: age
            3: population
            4: mayor
            """

    action_city: int = input(table)

    while action_city.isdigit() is False or (not (2 <= int(action_city) <= 3)):
        action_city: int = input('You can make age/population filter')

    less_big: int = input('less 1; bigger 2')
    while less_big.isdigit() is False or (not (1 <= int(less_big) <= 2)):
        less_big: int = input('You can write only 1 or 2')

    border: int = input('Write number, with that we will compare rest')

    while border.isdigit() is False:
        border: int = input('You can write only a number')

    cities_satisty_filter(int(action_city), int(less_big), int(border))

    return cities


def show_all_cities_info(cities: list) -> list:
    """ show all cities from the list and their properties """
    for city in cities:
        print(f"""
               name: {city.name}
               population: {city.population}
               age: {city.age}
               mayor: {city.mayor}
               """)

    return cities


def city_counter(cities: list) -> list:
    """ show how many cities currently in the list """
    print(f'Have {len(cities)} cities in our list')

    return cities


def main_menu(cities: list, action: int) -> list:
    switcher: dict = {
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

    table: str = """
            1: add city
            2: delete city
            3: change smth in city
            4: show city info
            5: city filter
            6: show all cities info
            7: city counter
            8: exit
            """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    action: int = input(table)

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while action.isdigit() is False or (not (0 < int(action) < 9)):
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action: int = input()

    if int(action) == 8:
        exit()
    cities = main_menu(cities, int(action))

    return cities


if __name__ == '__main__':
    cities: list = []
    file_path: None = None
    print('Choose the file')
    while file_path is None:
        file_path: str = str(input())

        try:
            with open(file_path, 'r'):
                pass

        except:
            print('cannot open file on this destination')
            file_path: None = None

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        lines: int = 0
        for row in csv_reader:
            if lines > 0 and row != []:
                city_name = City_17(int(row[0]), row[1], int(row[2]), row[3])
                cities.append(city_name)

            lines += 1
    [print(city.name) for city in cities]
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
