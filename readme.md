# MOOD Sense App (Windows & Raspbian Setup)

> Environmental sensor monitoring and annotation web app.

---

## 1. Prerequisites

### 🪟 For Windows

1. **Install Python 3.10+**
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Check “Add Python to PATH” during installation.

2. **Install InfluxDB**
   - Download from [InfluxDB Downloads](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.5.0-windows_amd64.zip?_gl=1*190aor1*_gcl_aw*R0NMLjE3NjE4MTM4MzUuQ2owS0NRandtWXpJQmhDNkFSSXNBSEEzSWtUV1RvUzg3NEZoc0pwazFGSEV3Q09hX3MyTXp4UDBUdzdhT2hNc2R1OTVoUXhmbDU0VkN6UWFBaW5xRUFMd193Y0I.*_gcl_au*MTYxODg0NDk5My4xNzYxODEzODM1*_ga*NTk3MDU2NzQ2LjE3NjE4MTM4MzM.*_ga_CNWQ54SDD8*czE3NjE4MTM4MzIkbzEkZzEkdDE3NjE4MTQ5NTAkajYwJGwwJGgxMjQyNzg3MjYx)

   - Extract the Files
   Extract the archive to a folder, for example:
   ```
   C:\Program Files\InfluxData\influxdb3-core
   ```
   - Open PowerShell as Administrator
   Press **Win + X → Windows PowerShell (Admin)**  
   Then navigate to the folder:
   ```powershell
   cd "C:\Program Files\InfluxData\influxdb3-core"
   ```
   - Run the InfluxDB 3 Server
   Start the server manually:
   ```powershell
   .\influxdb3.exe serve --node-id node01 --object-store=file --data-dir C:\InfluxData\influxdb-data
   ```

   - `--object-store=file` stores data locally on disk.  
   - `--data-dir` defines the data location.

   - Verify Installation
   Check version:
   ```powershell
   .\influxdb3.exe --version
   ```


3. **Create Database (Bucket)**
   - Create a bucket, e.g., `mood_sense` in InfluxDB UI.

4. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Set Environment Variables**
   Create a `.env` file in the project root e.g.:
   ```env
   HOST=https://192.168.0.101:8100/
   INFLUXDB=192.168.0.101
   ```

6. **(Optional) SSL Certificates**
   ```powershell
   openssl req -x509 -newkey rsa:4096 -keyout host.key -out host.cert -days 365 -nodes
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

3. **Set .env file e.g.**
   ```env
   HOST=https://192.168.0.101:8100/
   INFLUXDB=192.168.0.101
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
