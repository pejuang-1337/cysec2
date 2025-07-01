import requests

def run_scan(url):
    try:
        response = requests.get(url)
        result = f"[+] Header dari {url}:
"
        for k, v in response.headers.items():
            result += f"{k}: {v}\n"
        return result
    except Exception as e:
        return f"[ERROR] Gagal scan {url}: {str(e)}"