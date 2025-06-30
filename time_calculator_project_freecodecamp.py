def add_time(start, duration, days_of_the_week = ''):
    name_days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_later_str = ''
    new_day_of_the_week = ''
    parts = start.split(':')
    original_hour = int(parts[0])
    parts = parts[1].split(' ')
    original_minute = int(parts[0])
    AM_or_PM = parts[1]

    parts = duration.split(':')
    plus_hour = int(parts[0])
    plus_minute = int(parts[1])
    if AM_or_PM == 'PM':
        original_hour += 12

    whole_minutes = original_minute + plus_minute + (original_hour + plus_hour) * 60
    new_minute = whole_minutes % 60
    new_hour = (whole_minutes // 60) % 24
    days_later = (whole_minutes) // (60*24)

    if new_hour >= 12:
        AM_or_PM = 'PM'
    else:
        AM_or_PM = 'AM'

    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    if days_later == 1:
        days_later_str = ' (next day)'
    elif days_later > 1:
        days_later_str = ' (' + str(days_later) + ' days later)'

    days_of_the_week = days_of_the_week.lower()
    if days_of_the_week:
        index_day_of_the_week = name_days_of_the_week.index(days_of_the_week)
        new_day_of_the_week = name_days_of_the_week[(index_day_of_the_week + days_later) % 7].capitalize()

    if new_day_of_the_week:
        new_time = f'{new_hour}:{str(new_minute).rjust(2, "0")} {AM_or_PM}, {new_day_of_the_week}{days_later_str}'
    else:  
        new_time = f'{new_hour}:{str(new_minute).rjust(2, "0")} {AM_or_PM}{days_later_str}'
    
    return new_time


def main():
    print(add_time('3:30 PM', '2:12'))
    print(add_time('11:55 AM', '3:12'))
    print(add_time('2:59 AM', '24:00'))
    print(add_time('11:59 PM', '24:05'))
    print(add_time('8:16 PM', '466:02'))
    print(add_time('3:30 PM', '2:12', 'Monday'))
    print(add_time('2:59 AM', '24:00', 'saturDay'))
    print(add_time('11:59 PM', '24:05', 'Wednesday'))  
    print(add_time('8:16 PM', '466:02', 'tuesday')) 
    print(add_time('12:00 PM', '0:01'))

main()
