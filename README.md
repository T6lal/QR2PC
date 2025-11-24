# QR2PC
Short, perfect if you focus on QR sending to PC.


### Project: **Local Link-Opener Micro-Server**

A super-lightweight Python script that lets you fire URLs from your iPhone (or anything that can hit a web-hook) straight onto your Windows / macOS browser. Great for zapping links from iOS Shortcuts to your desktop without AirDrop or cloud syncing.

---

#### What it does

1. **Spins up an HTTP server** on `PORT = 8787`.
2. **Parses GET requests** like

   ```
   http://<PC-IP>:8787/open?url=https%3A%2F%2Fexample.com
   ```
3. **URL-decodes** the query and calls `webbrowser.open(url)` so the link pops open in your default browser.
4. Silences default HTTP logs for a clean console.

---

#### Quick start

```bash
# 1. Clone
git clone https://github.com/<you>/link-opener-server.git
cd link-opener-server

# 2. (Optional) create virtual env
python -m venv .venv && source .venv/bin/activate  # PowerShell: .venv\Scripts\Activate.ps1

# 3. Run
python link_opener.py
```

Console output will show something like:

```
Server started on IP: 192.168.1.42, port: 8787
Use this URL in your Shortcut: http://192.168.1.42:8787/open?url=
Waiting for links from iPhone...
```

---

#### iOS Shortcut snippet

1. **“URL Encode”** the input link.
2. **“Get Contents of URL”** → `GET` → `http://<PC-IP>:8787/open?url=`+EncodedURL
3. Done! Tapping the shortcut launches the link on your computer instantly.

---

#### Files

| File             | Purpose                            |
| ---------------- | ---------------------------------- |
| `link_opener.py` | Main script (shown above)          |
| `README.md`      | This documentation                 |
| `LICENSE`        | MIT by default—feel free to change |

---

#### Why this exists

* I kept emailing myself links or using clunky clipboard sync apps.
* Needed a **zero-install** solution on iOS (Shortcuts are pre-installed).
* Wanted full control (runs only on local LAN, no cloud middle-man).

---

#### Security notes

* **LAN-only by default** (binds to `""`, so firewalls/router keep it local).
* Don’t expose port 8787 to the public Internet unless you add auth.

---

#### TODO / Ideas

* Switch to `http.server.ThreadingHTTPServer` for concurrent hits.
* Add simple token-based auth header.
* Auto-generate the iOS Shortcut via `.shortcut` file export.
* Tray icon / installer for Windows users.

---

#### License

MIT – do anything, just leave attribution.
