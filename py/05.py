import fileinput

A = [line.strip() for line in fileinput.input()]

top_id = None
bot_id = None
seats = set()
for bp in A:
    r = 0
    rp = 64
    c = 0
    cp = 4
    for x in bp:
        if x == 'F':
            rp //= 2
        if x == 'B':
            r += rp
            rp //= 2
        if x == 'L':
            cp //= 2
        if x == 'R':
            c += cp
            cp //= 2
    seat_id = r * 8 + c
    seats.add(seat_id)
    if not top_id or seat_id > top_id:
        top_id = seat_id
    if not bot_id or seat_id < bot_id:
        bot_id = seat_id

missing_seat = 0
for seat in range(bot_id, top_id):
    if seat not in seats:
        missing_seat = seat

print('Part 1:', top_id)
print('Part 2:', missing_seat)
