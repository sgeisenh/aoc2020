import fileinput

def p1_valid(passport):
    return all(key in passport
            for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def p2_valid(passport):
    if not p1_valid(passport):
        return False
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False
    if passport['hcl'][0] != '#':
        return False
    if not all('0' <= char <= '9' or 'a' <= char <= 'f' for char in passport['hcl'][1:]):
        return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not len(passport['pid']) == 9:
        return False
    if not all('0' <= char <= '9' for char in passport['pid']):
        return False
    return True

passport = {}
num_p1 = 0
num_p2 = 0
for line in fileinput.input():
    if len(line.strip()) == 0:
        if p1_valid(passport):
            num_p1 += 1
        if p2_valid(passport):
            num_p2 += 1
        passport = {}
        continue

    for field in line.split():
        k, v = field.split(':')
        passport[k] = v

if p1_valid(passport):
    num_p1 += 1
if p2_valid(passport):
    num_p2 += 1

print('Part 1:', num_p1)
print('Part 2:', num_p2)
