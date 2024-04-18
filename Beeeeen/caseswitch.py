def weekday_name(day):
    return match day:
        case 1:
            "Monday"
        case 2:
            "Tuesday"
        case 3:
            "Wednesday"
        case 4:
            "Thursday"
        case 5:
            "Friday"
        case 6:
            "Saturday"
        case 7:
            "Sunday"
        case _:
            "Invalid day"

#3.10 에서만 쓰는 match
