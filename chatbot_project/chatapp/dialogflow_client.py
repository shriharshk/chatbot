import requests

DIALOGFLOW_URL = 'https://api.dialogflow.com/v1/query?v=20150910'


def get_response(token: str, message: str, session_id: str) -> str:
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'lang': 'en',
        'query': message,
        'sessionId': session_id,
        'timezone': 'UTC',
    }
    resp = requests.post(DIALOGFLOW_URL, json=payload, headers=headers, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    return data.get('result', {}).get('fulfillment', {}).get('speech', '')
