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
    winning_moves = {"C": 1, "B": 3, "A": 2}
    drawing_moves = {"A": 1, "B": 2, "C": 3}
    losing_moves = {"A": 3, "C": 2, "B": 1}
    total_score = 0
    for row in lines:
        required_outcome = row[2]
        opponent_plays = row[0]
        if required_outcome == "X":  # you lose
            total_score += losing_moves[opponent_plays]
        elif required_outcome == "Y":  # you draw
            total_score += (3 + drawing_moves[opponent_plays])
        elif required_outcome == "Z":  # you win
            total_score += (6 + winning_moves[opponent_plays])
    print(total_score)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    pt1_scoring()
    pt2_moves()
