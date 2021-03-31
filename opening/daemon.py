from datetime import time, datetime, timedelta
from threading import Timer
from os import path
import pickle
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

    global config
    config = get_config()
    for i in config:
        i.run_timer()

    # I have to define it in here so the variables I need are in scope
    class MyHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            # This might not work
            new_config = get_config()
            for i in new_config:
                i.run_timer()
            # Reload the list of active timers
            global config
            for i in config:
                i.cancel_timer()
            config = new_config

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(
        event_handler,
        path=path.expanduser("~/.config/link_opening/"),
        recursive=False,
    )
    observer.start()

    # Ok this can run for a year it should be fine. Hacky but idk how to get it work properly
    # What this does is prevent the thread from dying when it reloads the config
    t = Timer(timedelta(days=365).total_seconds(), print)
    t.start()


if __name__ == "__main__":
    main()