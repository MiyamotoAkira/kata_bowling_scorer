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
            score += get_value(roll)
            if roll == '/':
                score -= get_spare_correction(line, i)
                score += get_spare_bonus(line, i)
            elif roll == 'X':
                score += get_strike_bonus(line, i)
        else:
            break
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






