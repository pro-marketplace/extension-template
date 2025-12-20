import os
import json


def handler(event: dict, context) -> dict:
    """Пример backend функции"""

    method = event.get('httpMethod', 'GET')

    # CORS
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': ''
        }

    # Секреты из переменных окружения
    api_key = os.environ.get('EXAMPLE_API_KEY')

    # Парсинг body
    body = json.loads(event.get('body', '{}')) if event.get('body') else {}

    # Твоя логика здесь
    result = {
        'message': 'Hello from example!',
        'received': body
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result)
    }
