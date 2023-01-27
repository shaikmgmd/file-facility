def str_to_month(month_string):
    if month_string == 'Jan':
        return '01'
    elif month_string == 'Feb':
        return '02'
    elif month_string == 'Mar':
        return '03'
    elif month_string == 'Apr':
        return '04'
    elif month_string == 'May':
        return '05'
    elif month_string == 'Jun':
        return '06'
    elif month_string == 'Jul':
        return '07'
    elif month_string == 'Aug':
        return '08'
    elif month_string == 'Sep':
        return '09'
    elif month_string == 'Oct':
        return '10'
    elif month_string == 'Nov':
        return '11'
    elif month_string == 'Dec':
        return '12'


def date_format(date):
    year = date.split(' ')[-1]
    day = date.split(' ')[2]
    month = str_to_month(date.split(' ')[1])
    return year+'-'+month+'-'+day
