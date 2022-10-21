from datetime import datetime


def _datetime_stamp() -> str:
    return datetime.now().strftime('%d.%m.%Y %H:%S')
