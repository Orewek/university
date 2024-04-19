import datetime
import os
import shutil


def choose_file(file_path: str) -> str:
    """ choose a path for file/folder """
    file_path: str = input()

    if os.path.exists(file_path) is False:
        print('This file/folder doesnt exist!')
        file_path: None = None

    else:
        print('Your file/folder was succsessfully found')

    return file_path


def print_absolute_path(file_path: str) -> str:
    """ output absolute path for file/folder """
    abs_path = os.path.abspath(file_path)
    print(f"""
           ABSOLUTE PATH
           -------------
            {abs_path}
           -------------
           """)

    return file_path


def show_files_in_folder(file_path: str) -> str:
    """ show all files into the folder """
    if os.path.isfile(file_path) is True:
        print('You must write a folder path')

    else:
        all_files: list = []
        for path in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, path)):
                all_files.append(path)
        print('Thats all files in folder')
        print(all_files)
    return file_path


def create_new_folder(file_path: str) -> str:
    """ create a new folder """
    if file_path is None:
        file_path: str = input()

    if os.path.exists(file_path) is True:
        print('You must write a new path')

    elif os.path.isfile(file_path) is True:
        print('Your new path mustnt looks like a file path')

    else:
        os.makedirs(file_path)
        print('New folder was succsessfully created')

    return file_path


def show_all_file_properties(file_path: str) -> str:
    """ show all information about the file """
    file_stats = os.stat(file_path)

    file_size = os.path.getsize(file_path)
    last_time_modified = os.path.getmtime(file_path)
    file_creation_time = os.path.getctime(file_path)

    last_time_modified = datetime.datetime.fromtimestamp(last_time_modified)
    file_creation_time = datetime.datetime.fromtimestamp(file_creation_time)

    print(f"""
           file size: {file_size}
           time of last modification: {last_time_modified}
           creation time: {file_creation_time}
           """)

    action: str = input('print "more" for additional info')
    if action == 'more':
        mean_table: str = """
                           st_mode the file type and permissions
                           st_ino the inode number
                           st_dev the device id
                           st_uid the file owner id
                           st_gid the file group id
                           st_size the file size
                           """
        print(mean_table)
        print(file_stats)
    return file_path


def create_file_copy(file_path: str) -> str:
    """ create a copy of the file """
    if "." in file_path:
        extension: list = file_path.split(".")
        copy_file_path = f'{extension[0]}_copy.{extension[1]}'

        new_path: str = input('Choose a file path for a copy')
        while os.path.exists(new_path) is False or os.path.isfile(new_path) is True:
            new_path: str = input('You should write a competely a new path for that copy')

        shutil.copy(file_path, copy_file_path)
        os.replace(copy_file_path, rf'{new_path}\{copy_file_path}')

        print('copy was succsessfully created')

    else:
        shutil.copy(rf'{file_path}', rf'{file_path}_copy')
    return file_path


def show_all_spec_files_in_folder(file_path: str) -> str:
    """ show all files in folder with exact extension """
    if os.path.isfile(file_path) is True:
        print('You must write a folder path')
    else:
        all_files: list = make_files_list([], file_path)
        extension: str = input('Write an extension')
        if "." not in extension:
            extension = f'.{extension}'

        [print(file) for file in all_files if extension in file]

    return file_path


def delete_file_or_folder(file_path: str) -> None:
    """ delete file/folder """
    if os.path.isfile(file_path) is True:
        os.remove(file_path)
        return None

    all_files: list = make_files_list([], file_path)
    yes_confirmation: list = ['y', 'yes', 'yeah']
    for file in all_files:
        confirmation: str = input(f'Do you want to delete {file}? Write Y/N')
        if confirmation.lower() in yes_confirmation:
            os.remove(rf'{file_path}\{file}')

    all_files: list = make_files_list([], file_path)
    if all_files == []:
        os.rmdir(file_path)
    else:
        print('You cant remove a dir which contains some files')

    return None


def make_files_list(all_files: list, file_path: str) -> list:
    """ make a list of files into the folder """
    all_files: list = [path for path in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, path))]

    return all_files


def find_file_in_folder(file_path: str) -> str:
    """ check does the folder contain some file """
    if os.path.isfile(file_path) is True:
        print('You must write a folder path')

    else:
        all_files: list = make_files_list([], file_path)
        file_name: str = input('Write a file_name that we are loooking for')
        if file_name in all_files:
            print(f'This folder does contains {file_name}')
        else:
            print(f'This folder doesnt contains {file_name}')

    return file_path


def main_menu(file_path: str, action: int) -> str:
    switcher: dict = {
        1: choose_file,
        2: print_absolute_path,
        3: show_files_in_folder,
        4: show_all_file_properties,
        5: create_new_folder,
        6: create_file_copy,
        7: show_all_spec_files_in_folder,
        8: delete_file_or_folder,
        9: find_file_in_folder,
    }
    if file_path is None and (action != 1 and action != 5):
        print('You didnt write a file path, nothing to read!')
        return None

    file_path: str = str(switcher[action](file_path))

    return file_path


def main(file_path: str) -> str:
    table: str = """
            1: choose file to work with
            2: show absolute path for file/folder
            3: show all files in folder
            4: show all information about file
            5: make a new folder
            6: make a copy of file
            7: show all special files in folder
            8: delete file/folder
            9: find file in folder
            """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    action: int = input(table)

    while action.isdigit is False or (not (1 <= int(action) <= 9)):
        if action != '-table':
            print(action_table)
        else:
            print(table)

        action = input()

    file_path = main_menu(file_path, int(action))

    return file_path


if __name__ == '__main__':
    file_path: None = None
    while True:
        file_path = main(file_path)
