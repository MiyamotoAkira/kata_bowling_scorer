def get_score_from_line(line):
    score = 0
    for roll in line:
        if roll in ['1','9']:
            score += int(roll)

    return score
