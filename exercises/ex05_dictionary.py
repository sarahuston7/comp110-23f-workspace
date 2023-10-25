"""Dictionary practice."""

__author__ = "730459812"

def invert(dictionary: dict[str,str]) -> dict[str,str]:
    """When given a dictionary, it will swap values and keys."""
    inverted_list: dict[str,str]  = {}
    for keys in dictionary:
        value = dictionary[keys]
        inverted_list[value] = keys
    duplicates_list: list(str) = []
    for keys in dictionary:
        duplicates_list.append(dictionary[keys])
        print(duplicates_list)
    index1: int = 0
    index2: int = 1
    while len(duplicates_list) > index2:
        if duplicates_list[index1] == duplicates_list[index2]:
            raise KeyError("Can't have two of the same keys!")
        else:
            index2 += 1
        index1 += 1
    return inverted_list


def favorite_color(dictionary: dict[str,str]) -> str:
    """When given a dictionary, it will return the most frequent color."""
    color_dict: dict[str,int] = {}
    i: int = 0
    best_color: str = ""
    for name in dictionary:
        if dictionary[name] in color_dict:
            color_dict[dictionary[name]] += 1
        else:
            color_dict[dictionary[name]] = 1
    for color in color_dict:
        if color_dict[color] > i:
            i = color_dict[color]
            best_color = color
    return best_color


def count(counter_list: list[str]) -> dict[str,int]:
    """When given a list, it will create a dictionary with unique values and the number of values it appeared."""
    new_dict: dict[str,int] = {}
    i: int = 0
    list_index: int = 0
    while len(counter_list) > list_index:
        new_dict[counter_list[list_index]] = 0
        list_index += 1
    #counting duplicates
    index8: int = 0
    while len(counter_list) > index8:
        index9: int = 0
        counter: int = 0
        while len(counter_list) > index9:
            if counter_list[index8] == counter_list[index9]:
                counter += 1
            index9 += 1
        new_dict[(counter_list[index8])] = counter
        index8 += 1
    return new_dict


def alphabetizer(abc_list: list[str]) -> dict[str, list[str]]:
    """Give a list and get all the words that start with the same letter."""
    new_abc: list[str] = str(abc_list).lower()
    print(new_abc)
    character_abc_list: list[str] = []
    i: int = 0
    abc_dict: dict[str, list[str]] = {}
    while len(abc_list) > i:
        abc_dict[abc_list[i][0]] = "O"
        i += 1
    print(abc_dict)
    for objects in abc_dict:
        listy: list[str] = []
        k: int = 0
        while len(abc_list) > k:
            t: int = 0
            if ord(str(objects)) == ord(abc_list[k][0]):
                listy.append(abc_list[k])
                print(listy)
                abc_dict[objects] = listy
            k += 1
    return abc_dict


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Function that can update a dictionary log of attendence given a day and student."""
    if day not in log:
        log[day] = []
    for days in log:
        if day == days:
            listy: list[str] = []
            listy.append(log[days])
            listy.append(student)
            log[days] = listy
            print(listy)
    return log

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Wednesday" , "Kaleb")
update_attendance(attendance_log, "Tuesday" , "Vrinda")
print(attendance_log)