import requests
import time

DENON_IP = "YOUR RECEIVER'S IP"
BASE = f"http://{DENON_IP}:11080"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE}/#/main"
})

def init_session():
    """Load main page to establish session cookies"""
    r = session.get(f"{BASE}/", timeout=5)
    print("Session initialized, status:", r.status_code)

def set_input(index: int):
    url = f"{BASE}/ajax/globals/set_config"
    params = {
        "type": 7,
        "data": f'<Source zone="1" index="{index}"></Source>',
        "_": int(time.time() * 1000)
    }

    r = session.get(url, params=params, timeout=5)
    print("Set input response:", r.status_code, r.text)

# ---- RUN ----
init_session()      # REQUIRED FIRST
set_input(4)        # 4 = PC for my receiver, change this as needed for input numbers you want
