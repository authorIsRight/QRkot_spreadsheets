from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"


def generate_spreadsheet_body():
    now_date_time = datetime.now().strftime(FORMAT)

    spreadsheet_body = {
        'properties': {
            'title': f'Отчет от {now_date_time}',
            'locale': 'ru_RU'
        },
        'sheets': [
            {
                'properties': {
                    'sheetType': 'GRID',
                    'sheetId': 0,
                    'title': 'Лист1',
                    'gridProperties': {
                        'rowCount': 100,
                        'columnCount': 11
                    }
                }
            }
        ]
    }

    return spreadsheet_body


def generate_table_values():
    now_date_time = datetime.now().strftime(FORMAT)
    [
        ['Отчёт от', {now_date_time}],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]