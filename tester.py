import requests

import concurrent
from concurrent.futures import ThreadPoolExecutor


API_URL_TO_TEST = "http://127.0.0.1:8000/api/buy/"

API_REQUEST_BODY = {"service_id": 1, "user_id": "1"}

API_AUTH = ("test","test")

REQUEST_TIMES = range(10)

MAX_WORKERS = 20

def api_call():
    r = requests.post(API_URL_TO_TEST, data=API_REQUEST_BODY, auth=API_AUTH)
    return r.json()


def test():
  with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
      future_to_url = {executor.submit(api_call) for i in REQUEST_TIMES}
      for future in concurrent.futures.as_completed(future_to_url):
          try:
              data = future.result()
              print(data)
          except Exception as e:
              print("Looks like something went wrong:", e)

