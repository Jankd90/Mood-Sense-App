# MOOD Sense App (Windows & Raspbian Setup)

> Environmental sensor monitoring and annotation web app.

---

## 1. Prerequisites

### 🪟 For Windows

1. **Install Python 3.10+**
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Check “Add Python to PATH” during installation.

2. **Install InfluxDB 2.x**
   - Download from [InfluxDB Downloads](https://portal.influxdata.com/downloads/)
   - Start service:
     ```powershell
     net start influxdb
     ```
   - Access: [http://localhost:8086](http://localhost:8086)

3. **Create Database (Bucket)**
   - Create a bucket, e.g., `mood_sense` in InfluxDB UI.

4. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Set Environment Variables**
   Create a `.env` file in the project root:
   ```env
   HOST=127.0.0.1
   INFLUXDB=localhost
   ```

6. **(Optional) SSL Certificates**
   ```powershell
   openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
   ```

---

### 🐧 For Raspbian

1. **Install Python and dependencies**
   ```bash
   sudo apt update && sudo apt install python3 python3-pip libglib2.0-dev libssl-dev
   pip3 install -r requirements.txt
   ```

2. **Install and start InfluxDB**
   ```bash
   wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
   source /etc/os-release
   echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
   sudo apt update && sudo apt install -y influxdb
   sudo systemctl enable --now influxdb
   ```

3. **Set .env file**
   ```env
   HOST=<raspberry_pi_ip>
   INFLUXDB=localhost
   ```

---

## 2. Running the Application

### On Windows
```powershell
python annotation_app.py
```

### On Raspbian
```bash
python3 annotation_app.py
```

Then open a browser to:  
👉 [https://localhost:8100](https://localhost:8100) or [http://<raspberry_ip>:8100](http://<raspberry_ip>:8100)

---

## 3. Troubleshooting
- If SSL not configured, remove `ssl_context` in the last line of `annotation_app.py`.
- Ensure InfluxDB is running and accessible at the host/port defined in `.env`.
- On Windows, avoid using `bluepy`—not supported. Only the annotation app works natively.

---

**Author:** Adapted setup by ChatGPT for Windows + Raspbian compatibility.
