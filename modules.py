import tkinter as tk
import json
import webbrowser


def conn(incorr="Enter server infos"):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"server-infos": {"HOST": "", "PORT": 0}}

    def submitBtn():
        try:
            port_value = int(portE.get())
            ip_value = ipE.get()

            if ip_value == "":
                portCheckL.config(text="invalid IP or PORT!", fg="red")
            else:
                data["server-infos"]["HOST"] = ipE.get()
                data["server-infos"]["PORT"] = port_value
                portCheckL.config(text="Success! Please restart the client script", fg="green")

        except ValueError:
            portCheckL.config(text="invalid IP or PORT!", fg="red")

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def helpBtn():
        url = "https://github.com/Skyrix-7/PySocketChat/tree/main#files"
        webbrowser.open(url)

    window = tk.Toplevel()
    window.title("Server Infos")
    window.geometry("450x500")
    window.resizable(False, False)
    window.config(bg="black")
    window.grab_set()

    try:
        icon = tk.PhotoImage(file="server.png")
        window.iconphoto(True, icon)
    except Exception:
        pass

    win_frame = tk.Frame(window, bg="black")
    win_frame.pack(expand=True)

    abwin_frame = tk.Frame(win_frame, bg="black")
    abwin_frame.pack(expand=True)
    ipL = tk.Label(abwin_frame, text=incorr, fg="white", bg="black").pack(side=tk.LEFT, padx=10)

    ip_frame = tk.Frame(win_frame, bg="black")
    ip_frame.pack(expand=True)

    ipLa = tk.Label(ip_frame, text="IP (Ipv4):", fg="white", bg="black").pack(side=tk.LEFT, padx=10)

    ipE = tk.Entry(ip_frame)
    ipE.insert(0, data["server-infos"]["HOST"])
    ipE.pack(side=tk.LEFT, padx=10, pady=10)

    port_frame = tk.Frame(win_frame, bg="black")
    port_frame.pack(expand=True)

    portL = tk.Label(port_frame, text="Port:", fg="white", bg="black").pack(side=tk.LEFT, padx=22)

    portE = tk.Entry(port_frame)
    portE.insert(0, data["server-infos"]["PORT"])
    portE.pack(side=tk.LEFT, padx=10, pady=10)

    sub_frame = tk.Frame(win_frame, bg="black")
    sub_frame.pack(expand=True)

    portCheckL = tk.Label(window, text="", bg="black")
    portCheckL.pack(side=tk.BOTTOM, padx=22)

    submit = tk.Button(sub_frame, text="Submit", command=submitBtn).pack(side=tk.LEFT, pady=10, padx=10)
    help = tk.Button(sub_frame, text="help", command=helpBtn).pack(side=tk.RIGHT, pady=10, padx=10)

    window.wait_window()
