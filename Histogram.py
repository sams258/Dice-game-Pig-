class Histogram:
    def __init__(self, values):
        self.values = values
        self.counts = [self.values.count(i) for i in range(1, 7)]

    def __str__(self):
        lines = []
        for i in range(1, 7):
            lines.append(f"{i}: {'*' * self.counts[i-1]}")
        return "\n".join(lines)
