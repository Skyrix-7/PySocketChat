import socket
import tkinter as tk
import json
from termcolor import colored
import time
from modules import conn
import webbrowser
import sys

with open('data.json', 'r') as f:
    data = json.load(f)


HEADER = 64
PORT = data["server-infos"]["PORT"]
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
HOST = data["server-infos"]["HOST"]
ADDR = (HOST, PORT)


client = None
try:
    print("Connecting to " + colored(f"{HOST}:{PORT}", "cyan"))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)
    client.connect(ADDR)
    client.settimeout(None)
except (socket.error, socket.timeout) as error:
    print(colored(f"Connection failed: {error}", "red"))
    conn("HOST and PORT are incorrect, please change them below!")
    sys.exit(1)


def sendBtnf():
    text = sendBox.get()
    send(text)

def githubBtnf():
    webbrowser.open_new_tab("https://github.com/Skyrix-7/PySocketChat/")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if msg == DISCONNECT_MSG:
        time.sleep(1)
        statusL.config(text="Not Connected", fg="red")
        label2.config(text="Disconnected", fg="red")
        label3.config(text="to reconnect, please restart the client script!", fg="gray")
        client.close()
    else:
        sendBox.delete(0, tk.END)
        label2.config(text=client.recv(2048).decode(FORMAT), fg="green")

def connBtnf():
    conn()

def enter(event):
    sendBtnf()
    sendBox.delete(0, tk.END)

def on_focus_in(event):
    if sendBox.get().strip() == "Enter a message to send to server...":
            sendBox.delete(0, tk.END)
            sendBox.config(fg='black')

def on_focus_out(event):
    if sendBox.get() == "":
            sendBox.insert(0, "Enter text here...")
            sendBox.config(fg='grey')

root = tk.Tk()

try:
    icon = tk.PhotoImage(file="server.png")
    root.iconphoto(True, icon)
except Exception:
    pass

root.title("Contact Server")
root.geometry("1080x550")
root.configure(bg='black')
root.bind('<Return>', enter)

header = tk.Frame(root, bg="gray")
header.pack(side=tk.TOP)

statusL = tk.Label(header, text=f"Connected to {HOST}:{PORT}", fg="black", width=1000)
statusL.config(text="Connected", fg="green")
statusL.pack(side=tk.RIGHT)

first_frame = tk.Frame(root, bg="black")
first_frame.pack(expand=True)

label1 = tk.Label(first_frame, text="To disconnect type: !DISCONNECT", fg="white", bg="black")
label1.pack()

send_frame = tk.Frame(root, bg="black")
send_frame.pack(expand=True)

sendBox = tk.Entry(send_frame, width=100)
sendBox.insert(0, "Enter a message to send to server...")
sendBox.bind("<FocusIn>", on_focus_in)
sendBox.bind("<FocusOut>", on_focus_out)
sendBox.pack(side=tk.LEFT, pady=10, padx=10)

sendBtn = tk.Button(send_frame, text="SEND", command=sendBtnf)
sendBtn.pack(side=tk.LEFT)

bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack(expand=True, side=tk.BOTTOM, pady=50)

connBtn = tk.Button(bottom_frame, text="Change server", command=connBtnf)
connBtn.pack(side=tk.LEFT, padx=10)

githubBtn = tk.Button(bottom_frame, text="Github", command=githubBtnf)
githubBtn.pack(side=tk.LEFT, padx=10)

label2 = tk.Label(root, text="", bg="black")
label2.pack()

label3 = tk.Label(root, text="", bg="black")
label3.pack()

root.mainloop()
