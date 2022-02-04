from datetime import datetime
from anyio import sleep
import argparse
from time import time, sleep
from urllib import request
from urllib.error import HTTPError
import json


def get(url):
    with request.urlopen(url) as r:
        data = r.read()
        data
    return json.loads(data), r


class DelayRequest:
    def __init__(self, delay=1) -> None:
        self.last = time()
        self.delay = delay

    def __call__(self):
        try:
            sleep(self.delay - (time() - self.last))
        except ValueError:
            pass
        self.last = time()


def test_endpoint(url, seconds=10, interval=0.04):
    all_data = []
    start = time()
    req_last = start
    delay = DelayRequest(interval)
    req_time = []
    while (time() - start) <= seconds:
        # r = requests.get(url)
        try:
            data, r = get(url)
            data["status"] = 200
            all_data.append(data)
            print("↓", end="", sep="", flush=True)
        except HTTPError as e:
            data = {
                "url": url,
                "now": datetime.utcnow().isoformat(),
                "status": e.code,
            }
            all_data.append(data)
            print("⇡", end="", sep="", flush=True)
        req_now = time()
        req_time.append(req_now - req_last)
        req_last = req_now
        delay()
    return req_time, all_data


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--url", required=True)
    ap.add_argument("-t", "--time", required=False, default=2)
    ap.add_argument("-i", "--interval", required=False, default=0.5)
    args = ap.parse_args()

    url = str(args.url)
    t = int(args.time)
    i = float(args.interval)

    if not url.startswith("http://"):
        url = f"http://{url}"

    req_time, all_data = test_endpoint(url, seconds=t, interval=i)

    print(f"\nRate         : {len(all_data)/t:.1f} r/s")
    print(f"Time/request : {t/len(all_data):.3f} s/r")
    print(f"Success [200]: {sum([1 for x in all_data if x['status'] == 200])}")
    print(f"Fail    [503]: {sum([1 for x in all_data if x['status'] == 503])}")
    print(f"Total        : {len(all_data):.0f}")
