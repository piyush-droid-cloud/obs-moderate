import requests, random, time

endpoints = ["/", "/about", "/health", "/error", "/slow", "/items"]

def simulate_traffic():
    while True:
        endpoint = random.choice(endpoints)
        try:
            requests.get(f"http://localhost:5000{endpoint}", timeout=10)
        except Exception as e:
            print("Traffic generator error:", e)
        time.sleep(random.uniform(1, 3))  # 1–3 sec between requests
