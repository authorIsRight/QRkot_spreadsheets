from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"

NOW_DATE_TIME = datetime.now().strftime(FORMAT)

SPREADSHEET_BODY = {
    'properties': {
        'title': f'Отчет от {NOW_DATE_TIME}',
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