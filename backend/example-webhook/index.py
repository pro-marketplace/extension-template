import os
import json


def handler(event: dict, context) -> dict:
    """Пример webhook функции для приёма уведомлений от внешних сервисов"""

    method = event.get('httpMethod', 'POST')

    # CORS
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': ''
        }

    # Парсинг данных от внешнего сервиса
    body = json.loads(event.get('body', '{}')) if event.get('body') else {}

    # Твоя логика обработки webhook
    # Например: обновить статус в БД, отправить уведомление

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'body': 'OK'
    }
