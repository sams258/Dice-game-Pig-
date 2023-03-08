from pig.Print import Print


class Histogram:
    rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def add_roll(cls, roll):
        cls.rolls[roll] += 1

    @classmethod
    def clear(cls):
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def display(cls):
        Print.print_sleep("Histogram of Rolls:")
        for roll, count in cls.rolls.items():
            Print.print_sleep(f"{roll}: {'*' * count}")

    @classmethod
    def set_cheat(cls):
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
