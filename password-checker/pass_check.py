import requests
import hashlib
import sys

'''
Password checker - A simple script to check whether the 
password provided as input has been pawned before or not
'''


def request_api_data(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f"Error fetching {resp.status_code}. Kindly check the API and try again")
    return resp.text


def check_resp(hashes, hash_to_be_checked):
    data = {line.split(":")[0]: line.split(":")[1] for line in hashes.splitlines()}
    if hash_to_be_checked in data.keys():
        return data[hash_to_be_checked]
    else:
        return 0


def pwned_pwd_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    query_char, tail = sha1password[:5], sha1password[5:]
    hash_str = request_api_data(query_char)
    return check_resp(hash_str, tail)


if __name__ == "__main__":
    password_list = sys.argv[1:]
    for password in password_list:
        count = pwned_pwd_check(password)
        if count != 0:
            print(f"{password} is not safe...Have been found in {count} sites")
        else:
            print(f"{password} is absolutely safe")

