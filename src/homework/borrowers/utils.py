import datetime as dt


def get_current_utc():
    return dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
