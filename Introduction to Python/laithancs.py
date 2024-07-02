day, month, year = 2, 7, 2024
duration_days = 30

days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

days_left_in_month = days_in_month[month] - day + 1

if duration_days <= days_left_in_month:
    departure_day = day + duration_days - 1
    departure_month = month
    departure_year = year
else:
    remaining_days = duration_days - days_left_in_month
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

    departure_day = remaining_days
    departure_month = month
    departure_year = year

departure_date_str = f"{departure_day:02d}/{departure_month:02d}/{departure_year}"

print("Korean Friends will Depart On:", departure_date_str)
