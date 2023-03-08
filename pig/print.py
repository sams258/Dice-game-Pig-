import time


class Print:
    def __init__(self):
        pass

    def print_sleep(*args, **kwargs):
        print(*args, **kwargs)
        print()
        time.sleep(1)
