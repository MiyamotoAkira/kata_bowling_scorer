def get_value(roll):
    if roll == '-':
        return 0
    elif roll == 'X':
        return 10
    elif roll == '/':
        return 10
    else:
        return int(roll)


# 1. Passes tests
# 2. Minimizes duplication
# 3. Describes intent (clarity)
# 4. Simple

def get_score_from_line(line):
    score = 0
    for i, roll in enumerate(line):
        if is_standard_roll(line, i):
            if roll == 'X':
                score += 10
            elif roll == '-':
                score += 0
            elif roll == "/":
                score += 10 - get_value(line[i-1])
            else:
                score += int(roll)

        if i > 0 and line[i-1] == '/':
            score += get_value(roll)
        elif (i > 0 and line[i-1] == 'X') or (i > 1 and line[i-2] == 'X'):
            score += get_value(roll)

    return score

def is_standard_roll(line, current_roll_number):
    return get_frame(line[:current_roll_number+1]) <= 10

def get_spare_correction(line, current_roll_number):
    return get_value(line[current_roll_number-1])


def get_spare_bonus(line, current_roll_number):
    return get_value(line[current_roll_number+1]) 

def get_strike_bonus(line, current_roll_number):
    return get_value(line[current_roll_number+1]) + get_value(line[current_roll_number+2])


def get_frame(line):
    current_frame = 0
    half_frame = False
    for roll in line:
        if roll == 'X':
            current_frame += 1
        else:
            if half_frame:
                half_frame = False
            else:
                current_frame += 1
                half_frame = True
        
    return current_frame 






