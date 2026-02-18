import requests as rq

def obtener_dinosaurios():
    url = 'https://dinoapi.brunosouzadev.com/api/dinosaurs'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = rq.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except rq.RequestException as e:
        print(f"Error al conectar con la api: {e}")
        return []


