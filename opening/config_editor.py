import pickle
from os import path
import datetime
import pytz


class Link:
    def __init__(self, date, space, link):
        self.date = date
        self.space = space
        self.link = link

    def __str__(self):
        return (
            "starts at "
            + str(self.date)
            + " repeating every "
            + str(self.space)
            + " opening "
            + self.link
        )


def get_config():
    config_path = path.expanduser("~/.config/link_opening/links")
    try:
        return pickle.load(open(config_path, "rb"))
    except:
        # I know this is bad
        return []


def save_config(config):
    config_path = path.expanduser("~/.config/link_opening/links")
    pickle.dump(config, open(config_path, "wb"))


def add_link():
    config = get_config()
    time_to_run = input(
        "Enter the first date to run the link opening (YYYY-MM-DD HH:MM:SS):  "
    )
    days = int(input("Enter the number of days between runs: "))
    hours = int(input("Enter the number of hours between runs: "))
    minutes = int(input("Enter the number of minutes between runs: "))
    seconds = int(input("Enter the number of seconds between runs: "))
    time_between_runs = datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )
    time_to_run = datetime.datetime.strptime(time_to_run, "%Y-%m-%d %H:%M:%S")
    link = input("Enter your link:  ")
    link = Link(time_to_run, time_between_runs, link)
    config.append(link)
    save_config(config)


def remove_link():
    # Display as a list then ask for index to remove. Add pagination later but it's not important
    config = get_config()
    for (i, k) in enumerate(config):
        print(str(i) + ":", str(k))
    thing_to_delete = input("Enter the index of the thing you want to delete: ")
    thing_to_delete = int(thing_to_delete)
    config.pop(thing_to_delete)
    save_config(config)


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