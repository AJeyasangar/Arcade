import csv
import string

class Score:
    def __init__(self, game):
        self.game = game
        if self.game == "snake":
            self.path = "snake.txt"
        elif self.game == "breakout":
            self.path = "breakout.txt"

    def save_score(self, score):
        with open(self.path, "a", newline="") as myFile:
            writer = csv.writer(myFile)
            writer.writerow([score])
        myFile.close()

    def high_score(self):
        csvFile = csv.reader(open(self.path, 'r'))
        score_list = []
        for row in csvFile:
            score_list.append(row)
        max_score = max(score_list)
        max_score = (str(max_score).translate(str.maketrans('', '', string.punctuation)))
        return max_score
