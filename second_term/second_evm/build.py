import datetime
import os


def read_from_file(file_path: str) -> str:
    """ read and print infirmation from file """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)

    return file_path


def write_into_file(file_path: str) -> str:
    """ write some data into file """
    with open(file_path, 'a+') as f:
        data = str(input())
        f.write(data)

    print('data was successfully added to the end of the file')
    return file_path


def delete_from_file(file_path: str) -> str:
    """ delete all information from file """
    with open(file_path, 'w'):
        pass

    print('all data into file was successfully deleted')
    return file_path


def find_in_file(file_path: str) -> str:
    """
    find line, which continet data
    if file doesnt continet, notificate about it
    """
    find_data = str(input())
    with open(file_path, 'r') as f:
        lines = f.readlines()
        i = 1
        found_flag = 0
        for line in lines:
            if find_data in line:
                print(f'found {find_data} in {i}th line')
                found_flag += 1

        if found_flag == 0:
            print(f'file doesnt continet {find_data}')

    return file_path


def choose_file(file_path: str) -> str:
    """ write path to file """
    file_path = str(input())

    try:
        with open(file_path, 'r'):
            pass

    except:
        print('cannot open file on this destination')
        file_path = None

    return file_path


def calculate_time(file_path: str) -> str:
    """ how much time elapsed since last change """

    m_time = os.path.getmtime(file_path)
    # convert timestamp into DateTime object
    dt_m = datetime.datetime.fromtimestamp(m_time)
    print(f'{file_path} was modified on:', dt_m)

    return file_path


def main_menu(file_path: str, action: int) -> str:
    switcher = {
        1: read_from_file,
        2: write_into_file,
        3: delete_from_file,
        4: find_in_file,
        5: choose_file,
        6: calculate_time,
    }
    if file_path is None and action != 5:
        print('You didnt write a file path, nothing to read!')
        return None

    file_path = switcher[action](file_path)

    return file_path


def main(file_path: str) -> str:
    table = """
            1: read file
            2: write into file
            3: delete from file
            4: find in file
            5: choose file
            6: calculate time
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
    while len(action) != 1 or action.isdigit() is False or (not (0 < int(action) < 7)):
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action = input()

    file_path = main_menu(file_path, int(action))

    return file_path


if __name__ == '__main__':
    file_path = None
    while True:
        file_path = main(file_path)
