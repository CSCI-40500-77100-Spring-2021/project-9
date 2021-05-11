import requests

SERVER_URL = "143.244.222.9"
RECORD_ENDPOINT = "/record"

# Make a request to the telemetry server using the requests library.
# It's gonna be a POST request to /record.
def record_usage(method, size, duration_ms):
    data = {"method": method, "size": size, "duration_ms": duration_ms}
    requests.post("http://" + SERVER_URL + RECORD_ENDPOINT, data = data)