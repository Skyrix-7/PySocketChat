# PyRecap

A simple TCP client-server messaging app built with Python sockets and Tkinter.

![image alt](https://github.com/Skyrix-7/PySocketChat/blob/c4663e27c816da29457a6daf8008cc278c52bb98/preview.png)

## Features

- Start a server on a custom port and accept multiple clients via threading
- GUI client to connect, send messages, and receive acknowledgements
- In-app dialog to change the server HOST/PORT and save to `data.json`
- Disconnect with `!DISCONNECT`

## Usage

1. Install the dependency:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
python server.py
```

You will be prompted for a port and whether to auto-assign the address to `data.json`.

3. Start the client:

```bash
python client.py
```

4. (Optional) Click **Change server** to update the IP/port, then restart the client.

## Files

| File          | Purpose                              |
|---------------|--------------------------------------|
| `server.py`   | TCP server (multi-client, threaded)  |
| `client.py`   | Tkinter GUI client                   |
| `modules.py`  | Shared UI dialog for server config   |
| `data.json`   | Stores HOST and PORT for the client  |
| `requirements.txt` | Python dependencies             |
