from datetime import time, datetime, timedelta
from threading import Timer
from os import path
import pickle
import webbrowser


# Cool thing here, class instance data is serialized but the class itself is not, means I can have different class methods for the different things
class Link:
    def __init__(self, date, space, link):
        self.date = date
        self.space = space
        self.link = link

    def run_timer(self):
        # first run of the timer
        now = datetime.now()
        while now > self.date:
            self.date += self.space
        # redoing incase this takes lots of time - just find how many seconds away date is1`
        delta_t = self.date - datetime.now()
        secs = delta_t.total_seconds()
        self.timer = Timer(secs, self.run_link)
        self.timer.start()

    def cancel_timer(self):
        self.timer.cancel()

    def run_link(self):
        webbrowser.open(self.link)
        # Set a timer for the interval
        self.timer = Timer(self.space.total_seconds(), self.run_link)
        self.timer.start()


def get_config():
    config_path = path.expanduser("~/.config/link_opening/links")
    try:
        return pickle.load(open(config_path, "rb"))
    except:
        return []


def run_link(**kwargs):
    delta_t = timedelta(days=1)
    t = Timer(delta_t.total_seconds(), run_link, kwargs=kwargs)
    t.start()
    webbrowser.open(kwargs["link"])
    # Runs a link and then handles resuming timers


def main():
    print("Hello, world!")
    config = get_config()
    for i in config:
        i.run_timer()
    # First run - setup timers


if __name__ == "__main__":
    main()