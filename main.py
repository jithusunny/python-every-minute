#!/usr/bin/env python3
import requests

def main():
    response = requests.get("https://hit-every-minute.free.beeceptor.com/")
    print("Pinged; status code:", response.status_code)

if __name__ == "__main__":
    main()
