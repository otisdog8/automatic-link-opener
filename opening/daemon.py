from datetime import time, datetime, timedelta
from threading import Timer
from os import path
import pickle
import webbrowser


def get_config_dict():
    config_path = path.expanduser("~/.config/link_opening/links")
    try:
        return pickle.load(open(config_path, "rb"))
    except:
        return {}


def get_link_times():
    # Reads the config and figures out when to run what
    time_link_dict = {}

    return time_link_dict


def run_link(**kwargs):
    delta_t = timedelta(days=1)
    t = Timer(delta_t.total_seconds(), run_link, kwargs=kwargs)
    t.start()
    webbrowser.open(kwargs["link"])
    # Runs a link and then handles resuming timers


def main():
    print("Hello, world!")
    config_dict = get_config_dict()
    for (k, v) in config_dict.items():
        x = datetime.today()
        # Happens before today, or happens after today
        y = x.replace(
            day=x.day,
            hour=k.hour,
            minute=k.minute,
            second=k.second,
            microsecond=k.microsecond,
        )
        if x > y:
            y += timedelta(days=1)
        else:
            pass
        delta_t = y - x
        secs = delta_t.total_seconds()
        arguments = {}
        arguments["time"] = k
        arguments["link"] = v
        t = Timer(secs, run_link, kwargs=arguments)
        t.start()

    # First run - setup timers


if __name__ == "__main__":
    main()