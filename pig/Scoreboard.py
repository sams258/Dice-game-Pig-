import json


class Scoreboard:
    def __init__(self):
        self.scores = {}
        self.load_scores()

    def add_score(self, name, score):
        if name in self.scores:
            self.scores[name]["scores"].append(score)
            self.scores[name]["games_played"] += 1
        else:
            self.scores[name] = {"scores": [score], "games_played": 1}
        self.save_scores()

    def get_high_scores(self):
        high_scores = []
        for name, data in self.scores.items():
            high_score = max(data["scores"])
            high_scores.append((name, high_score, data["games_played"]))
        high_scores.sort(key=lambda x: x[1], reverse=True)
        return high_scores

    def load_scores(self):
        try:
            with open("scores.json", "r") as f:
                self.scores = json.load(f)
        except:
            self.scores = {}

    def save_scores(self):
        with open("scores.json", "w") as f:
            json.dump(self.scores, f)

    def get_player_score(self, name):
        if name in self.scores:
            return sum(self.scores[name]["scores"])
        return 0

    def change_player_name(self, old_name, new_name):
        if old_name in self.scores:
            self.scores[new_name] = self.scores.pop(old_name)
            self.save_scores()

    def clear(self):
        self.scores = {}
        self.save_scores()
