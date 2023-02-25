class Highscore:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lessthan__(self, other):
        return self.score < other.score

    def __greaterthan__(self, other):
        return self.score > other.score

    def __equal__(self, other):
        return self.score == other.score

    def __lessthanorequal__(self, other):
        return self.score <= other.score

    def __greaterthanorequal__(self, other):
        return self.score >= other.score

    def __notqual__(self, other):
        return self.score != other.score

    def __str__(self):
        return self.name + " " + str(self.score)

    def __repr__(self):
        return self.name + " " + str(self.score)
