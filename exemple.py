import requests
from typing import Optional


def get_reese_cookie(url : str) -> Optional[str]: 
    data = {
        'url': url
    }
    response = requests.post('http://localhost:3000/generate', data=data, timeout=10)
    if response.status_code == 200:
        return response.json()["cookie"]
    else:
        return None