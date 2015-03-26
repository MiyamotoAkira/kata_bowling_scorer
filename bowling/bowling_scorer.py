def get_value(roll):
    if roll == '-':
        return 0
    elif roll == 'X':
        return 10
    elif roll == '/':
        return 10
    else:
        return int(roll)

def get_score_from_line(line):
    score = 0
    for i, roll in enumerate(line):
        if roll == '/':
            score = score - get_value(line[i-1]) + get_value(roll)
        else:
            score += get_value(roll)

    return score
