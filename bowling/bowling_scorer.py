# Possible things to refactor
# - lots of functions using line, introduce a line object?

def get_value(roll):
    if roll == '-':
        return 0
    elif roll == 'X':
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
        if roll == "/":
            roll = 10 - get_value(line[i-1])
        
        if is_standard_roll(line, i):
            score += get_value(roll)

        if is_part_of_spare_bonus(line, i):
            score += get_value(roll)
        
        if is_part_of_strike_bonus(line, i):
            score += get_value(roll)

    return score

def is_part_of_spare_bonus(line, roll_number):
    return get_previous_roll(line, roll_number) == '/'

def is_part_of_strike_bonus(line, roll_number):
    return get_previous_roll(line, roll_number) == 'X' or get_roll_before_last(line, roll_number) == 'X'

def get_previous_roll(line, roll_number):
    return line[roll_number-1] if roll_number > 0 else None

def get_roll_before_last(line, roll_number):
    return roll_number > 1 and line[roll_number-2]

def is_standard_roll(line, current_roll_number):
    return get_frame(line[:current_roll_number+1]) <= 10

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






