# 6 Cinema Tickets
name_break = False
student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0

while not name_break:
    name = input()
    if name == "Finish":
        name_break = True
        break
    movie_tickets = 0
    free_seats = int(input())
    for seats in range(0, free_seats):
        type_seat = input()
        if type_seat == 'student':
            student_count += 1
            movie_tickets += 1
            total_tickets += 1
        elif type_seat == 'standard':
            standard_count += 1
            movie_tickets += 1
            total_tickets += 1
        elif type_seat == 'kid':
            kid_count += 1
            movie_tickets += 1
            total_tickets += 1
        else:
            break
    print(f'{name} - {((movie_tickets / free_seats) * 100):.2f}% full.')
print(f'Total tickets: {total_tickets}')
print(f'{((student_count / total_tickets) *100):.2f}% student tickets.')
print(f'{((standard_count / total_tickets) *100):.2f}% standard tickets.')
print(f'{((kid_count / total_tickets) *100):.2f}% kids tickets.')
