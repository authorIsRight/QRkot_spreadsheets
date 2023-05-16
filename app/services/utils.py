from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"


def current_time():
    return datetime.now().strftime(FORMAT)


SPREADSHEET_BODY = {
    'properties': {
        'title': f'Отчет от {current_time()}',
        'locale': 'ru_RU'
    },
    'sheets': [{'properties': {
        'sheetType': 'GRID',
        'sheetId': 0,
        'title': 'Лист1',
        'gridProperties': {'rowCount': 100,
                           'columnCount': 11}
    }}]
}
