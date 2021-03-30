import pickle
from os import path
from datetime import time, tzinfo
import pytz


def get_config_dict():
    config_path = path.expanduser("~/.config/link_opening/links")
    try:
        return pickle.load(open(config_path, "rb"))
    except:
        return {}


def save_config_dict(dictionary):
    config_path = path.expanduser("~/.config/link_opening/links")
    pickle.dump(dictionary, open(config_path, "wb"))


def add_link():
    config_dict = get_config_dict()
    time_to_run = input(
        "Enter your time (hh:mm:ss), hours are in military time and PST. If there are multiple at the same time put them at different seconds:  "
    )
    link = input("Enter your link:  ")
    timezone = pytz.timezone("America/Los_Angeles")
    split_time = time_to_run.split(":")
    hour = int(split_time[0])
    minute = int(split_time[1])
    second = int(split_time[2])
    time_to_run = time(hour, minute, second, 0, timezone)
    config_dict[time_to_run] = link
    save_config_dict(config_dict)


def remove_link():
    # Display as a list then ask for index to remove. Add pagination later but it's not important
    config_dict = get_config_dict()
    keys = list(config_dict.keys())
    for (i, k) in enumerate(keys):
        print(str(i) + ":", k)
    thing_to_delete = input("Enter the index of the thing you want to delete: ")
    thing_to_delete = int(thing_to_delete)
    thing_to_delete = keys[thing_to_delete]
    del config_dict[thing_to_delete]
    save_config_dict(config_dict)


def main():
    while 1:
        choice = input(
            "Would you like to:\n1. Add a new link\n2. Remove an existing link\n3. Exit the program\n>  "
        )
        try:
            num = int(choice)
            if num == 1:
                add_link()
            elif num == 2:
                remove_link()
            elif num == 3:
                break
            else:
                pass

        except ValueError:
            pass


if __name__ == "__main__":
    main()