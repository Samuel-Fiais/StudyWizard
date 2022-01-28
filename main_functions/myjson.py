import json


def manipulate_json_file(path, option="r", data="None"):
    """
    Manipulate a json file.
    :param path: path of the json file.
    :param option: "r" for reading, "w" for writing, "a" for appending.
    :param data: data to write in the json file.
    :return: the json file.
    """

    if option == "r":
        info = json.load(open(path, "r"))
        return info
    elif option == "w":
        json.dump(data, open(path, "w"))
    elif option == "a":
        json.dump(data, open(path, "a"))

