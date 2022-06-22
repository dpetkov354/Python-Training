# 8 On Time for the Exam
exam_hour = int(input())
exam_minutes = int(input())
exam_time_minutes = (exam_hour * 60) + exam_minutes
arrival_hour = int(input())
arrival_minutes = int(input())
arrival_time_minutes = (arrival_hour * 60) + arrival_minutes
diff_minutes = abs(exam_time_minutes - arrival_time_minutes)
hours = diff_minutes // 60
minutes = diff_minutes % 60
if 23 >= exam_hour >= 0 and 59 >= exam_minutes >= 0 and 23 >= arrival_hour >= 0 and 59 >= arrival_minutes >= 0:
    if exam_hour == arrival_hour and exam_minutes == arrival_minutes:
        print("On time")
    elif exam_time_minutes > arrival_time_minutes and diff_minutes <= 30:
        print("On time")
        print(f'{minutes} minutes before the start')
    if exam_time_minutes > arrival_time_minutes and 60 > diff_minutes > 30:
        print("Early")
        print(f'{minutes} minutes before the start')
    elif exam_time_minutes > arrival_time_minutes and diff_minutes >= 60:
        print("Early")
        print(f'{hours}:{minutes:02d} hours before the start')
    if exam_time_minutes < arrival_time_minutes and 60 > abs(diff_minutes) >= 1:
        print("Late")
        print(f'{abs(minutes)} minutes after the start')
    elif exam_time_minutes < arrival_time_minutes and abs(diff_minutes) >= 60:
        print("Late")
        print(f'{abs(hours)}:{(abs(minutes)):02d} hours after the start')
else:
    quit()

# 9 Ski Trip
days = int(input())
type_of_room = input()
grade = input()
price = 0

if type_of_room == "room for one person":
    price = (days - 1) * 18.00
    if grade == "positive":
        price = price * 1.25
    else:
        price = price * 0.9
    print(f'{price:0.2f}')
if type_of_room == "apartment":
    price = (days - 1) * 25.00
    if days < 10:
        price = price * 0.7
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if 10 <= days <= 15:
        price = price * 0.65
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if days > 15:
        price = price * 0.5
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
if type_of_room == "president apartment":
    price = (days - 1) * 35.00
    if days < 10:
        price = price * 0.9
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if 10 <= days <= 15:
        price = price * 0.85
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if days > 15:
        price = price * 0.8
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
