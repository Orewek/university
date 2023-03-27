class city_17(object):
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
    name = str(input())

    population = input()
    while population.isdigit() is False:
        population = input()

    mayor = str(input())

    age = input()

    while age.isdigit() is False:
        age = input()

    name = city_17(int(population), mayor, int(age), name.capitalize())
    cities.append(name)

    return cities

def delete_city(cities: list) -> list:
    for count, city in enumerate(cities):
        print(count, city)

    return cities



def main() -> None:
    moscow = city_17(13_000_000, 'Sobyanin', 876, 'Moscow')
    washington = city_17(7_739_000, 'Barack Obama', 232, 'Washington')

    cities = [moscow, washington]

    table = """
            1: add city
            2: delete city
            3: change smth in city
            4: show city info
            5: city filter
            6: show all cities info
            7: city counter
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
    while len(action) != 1 or action.isdigit() is False or (not (0 < int(action) < 8)):
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action = input()

    file_path = main_menu(file_path, int(action))
    

if __name__ == '__main__':
    main()
