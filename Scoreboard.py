
class Highscore:
    
    def __init__(self):
        self.high_scores = []

    def add_score(self, name, score):
        self.high_scores.append((name, score))

    def get_high_scores(self):
        return sorted(self.high_scores, key=lambda x: x[1], reverse=True)[:10]
    

    """
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


