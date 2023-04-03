import os


def main_menu(file_path: str, action: int) -> str:
    switcher = {
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
    if file_path is None and action != 5:
        print('You didnt write a file path, nothing to read!')
        return None

    file_path = switcher[action](file_path)

    return file_path


def main() -> None:
    table = """
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

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """


if __name__ == '__main__':
    main()
