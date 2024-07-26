import requests as ss
import time, sys, os
from os import path

s = ss.Session()


def print_on_screen(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


os.system("cls" if os.name == "nt" else "clear")

check = path.exists("token_tube_rocket.txt")
if check == True:
    sua = input(f"Do you want to change the token? (y/n): ")
    if sua == "y":
        os.remove("token_tube_rocket.txt")
        a = open("token_tube_rocket.txt", "w")
        token = input("Please type your TubeRocket token: ")
        a.write(token)
        a.close()
    else:
        a = open("token_tube_rocket.txt", "r")
        token = a.readline()
else:
    a = open("token_tube_rocket.txt", "w")
    token = input("Please type your TubeRocket token: ")
    a.write(token)
    a.close()
# os.system('clear')

os.system("cls" if os.name == "nt" else "clear")

introduce = "This is Tool TubeRocket by Python.\n\
Thank you for running my tool.\n\
Happy you good day."
print_on_screen(introduce)

# os.system('clear')

# print_on_screen("Please type your TubeRocket token: ")
# token = "60f78250d93d11eeba85afaf21d82114"

os.system("cls" if os.name == "nt" else "clear")

headGetInfo = {
    "Host": "tuberocket.app:3000",
    "token": token,
}

getInfo = s.get("http://tuberocket.app:3000/api/member", headers=headGetInfo).json()
email = getInfo["result"]["email"]
coin = getInfo["result"]["coin"]
print_on_screen(email + " | " + str(coin))

print_on_screen("-----------------------------------")

headRunVideo = {
    "Host": "tuberocket.app:3000",
    "token": token,
    "Content-Length": "71",
    "Content-Type": "application/json; charset=UTF-8",
}

cnt = 0

while True:
    try:
        getVideo = s.get(
            "http://tuberocket.app:3000/api/video", headers=headGetInfo
        ).json()
        idVideo = getVideo["result"]["videoId"]
        timeVideo = getVideo["result"]["playSecond"]
    except:
        exit("Account is banned or token expired!")
    else:
        for i in range(timeVideo, 0, -1):
            print(f"please wait {i} seconds", end="           \r")
            time.sleep(1)

        dataReceiveCoin = {
            "id": idVideo,
            "playCount": 0,
            "playSecond": 0,
            "boost": 0,
            "status": "",
        }
        receive = s.put(
            "http://tuberocket.app:3000/api/video",
            headers=headRunVideo,
            json=dataReceiveCoin,
        ).json()
        received_coin = receive["result"]["coin"]
        cnt += 1
        print_on_screen(
            str(cnt) + " | " + " ID video " + idVideo + " | " + str(received_coin)
        )
