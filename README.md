# MacroPad App 🎹

Python client for talking to a macro pad over USB serial. The single script in this repo (`TestWritingToDevice.py`) scans for the macro pad among connected serial ports, opens it, writes a line to it, and prints the four lines the device sends back — a smoke test that the host ↔ device serial protocol actually round-trips.

## How it fits together

The whole project is one script plus a license:

```
├── TestWritingToDevice.py   # the entire app: find port → open → write → read 4 lines
└── LICENSE.txt              # GPL-3.0-only (copyright Lucas Oskorep)
```

There is no package structure, config, or dependency manifest — just the script.

### Where the real behavior lives

Everything is in `TestWritingToDevice.py`, and the interesting bit is device discovery:

- **Port identification**: it enumerates all COM ports via `serial.tools.list_ports` and picks the one whose `hwid` contains `"DF60BCA"` **and** whose product ID is `33032` (PID `0x8110`). That hard-coded hwid/PID pair is the fingerprint of this particular macro pad — swap those constants and the script talks to a different device.
- **Protocol exchange**: it opens the port at default baud rate, writes `b"hello!\n"`, then reads exactly four lines back and prints each raw and decoded as UTF-8. The "four lines" expectation is baked into the loop count, mirroring whatever fixed-length reply the firmware sends per request.
- **Platform caveat**: the discovery branch is commented as Windows-oriented ("Windows code for figuring out which port to grab"), since it relies on `port.hwid` being populated, which isn't guaranteed on Linux.

## Setup

No build step or manifest. Just install PySerial and run the script with the pad plugged in:

```bash
pip install pyserial
python TestWritingToDevice.py
```

Expect `FOUND MACROPAD!` followed by the device's reply lines if the pad is detected.

## Notes

- Licensed under GPL-3.0-only (`LICENSE.txt`, copyright Lucas Oskorep).
- Remote: `gitea.chaosdev.gay:lucasoskorep/macropados-client` — the "client" half of a presumably separate macro-pad OS/firmware project.
