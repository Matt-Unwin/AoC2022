def pt1_scoring():
    winning_moves = ["C X", "B Z", "A Y"]
    drawing_moves = ["A X", "B Y", "C Z"]
    scoring = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0
    for row in lines:
        you_play = row[2]
        if row in winning_moves:
            total_score += 6
        elif row in drawing_moves:
            total_score += 3
        total_score += scoring[you_play]
    print(total_score)


def pt2_moves():
    scores = {
        "X": {"A": 3, "C": 2, "B": 1},
        "Y": {"A": 4, "B": 5, "C": 6},
        "Z": {"C": 7, "B": 9, "A": 8}
    }
    total_score = 0
    for row in lines:
        required_outcome = row[2]
        opponent_plays = row[0]
        total_score += scores[required_outcome][opponent_plays]
    print(total_score)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    pt1_scoring()
    pt2_moves()
