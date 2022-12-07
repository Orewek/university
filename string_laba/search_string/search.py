def consistent_search(user_str: str, find_str: str) -> int:
    for i in range(len(user_str) - len(find_str)):
        if user_str[i:i + len(find_str)] == find_str:
            return i + 1

    return - 1


if __name__ == '__main__':
    print('You cant run this file as main')
