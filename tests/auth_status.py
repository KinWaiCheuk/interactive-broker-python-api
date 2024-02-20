import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def confirmStatus():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/auth/status"

    auth_req = requests.get(url=base_url+endpoint, verify=False)
    print(f"{auth_req=}")
    print(f"{auth_req.text=}")

if __name__ == "__main__":
    confirmStatus()