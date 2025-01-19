#!/usr/bin/python3
"""
json file
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        json_dta = response.json()
        if json_dta:
            print("[{}] {}".format(json_dta.get("id"), json_dta.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
