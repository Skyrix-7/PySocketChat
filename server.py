import socket
from termcolor import colored
import threading
import json

PORT = 0
choosedport = False

while not choosedport:
    try:
        zii = int(input("Enter a port for the server> "))
        if zii < 1 or zii > 65535:
            print(colored(f"{zii}: isn't a valid port! (1-65535)", "red"))
        else:
            print(colored("Success!", "green"))
            choosedport = True
            PORT = zii
    except ValueError:
        print(colored("Invalid input! Enter a number.", "red"))


HEADER = 64
HOST = socket.gethostbyname(socket.gethostname())

ADDR = (HOST, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


with open('data.json', 'r') as f:
    data = json.load(f)


choosed = False
while not choosed:
    innp = input("Do you want to auto assign HOST and PORT to client server infos (y or n)> ")

    if innp.lower() == "y":
        data["server-infos"]["HOST"] = HOST
        data["server-infos"]["PORT"] = PORT
        break
    elif innp.lower() == "n":
        break
    else:
        print(colored("Please choose between (y or n)", "red"))

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(socket.getaddrinfo(host=HOST, port=PORT))


def handleClient(conn, addr):
    print(f"{addr} is " + colored("Connected", "green"))
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONNECT_MSG:
                    connected = False
                    print(f"{addr} disconnected")
                else:
                    print(f"[{addr}]: {msg}")
                    succ = "Success!"
                    conn.send(succ.encode(FORMAT))
            else:
                connected = False
                print(f"{addr} disconnected")
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            print(f"{addr} " + colored("disconnected unexpectedly", "red"))
            connected = False
    conn.close()


def start():
    server.listen()
    print(f"Server is listening on " + colored(f"{HOST}:{PORT}", "yellow"))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")


start()
