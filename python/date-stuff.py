from datetime import date, datetime

import pytz


def datetime_now():
    uk_tz = pytz.timezone("Europe/London")
    return datetime.now() + uk_tz.localize(datetime.now()).utcoffset()


def month_diff(start_date, end_date):
    num_months = (end_date.year - start_date.year) * 12 + (
        end_date.month - start_date.month
    )
    return num_months


def years_and_months_between(start_date, end_date):
    if start_date is None or end_date is None:
        return None
    if type(start_date) == str:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if type(end_date) == str:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    months = month_diff(start_date, end_date)
    if months < 12:
        return f"{months} month" + ("" if months == 1 else "s")
    else:
        years = months // 12
        months = months % 12
        if months == 0:
            return f"{years} year" + ("" if years == 1 else "s")
        else:
            return (
                f"{years} year"
                + ("" if years == 1 else "s")
                + f" and {months} month"
                + ("" if months == 1 else "s")
            )


def format_date_string(date_string: str):
    # changes date that is in a string to a date and then to a formatted string
    return (
        datetime.strptime(date_string, "%Y-%m-%d").strftime("%d/%m/%Y")
        if date_string is not None
        else None
    )


def calculate_age(dob: date):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def month_name(month_num: int):
    return datetime(1, int(month_num), 1).strftime("%B")
