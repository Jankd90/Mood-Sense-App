from influxdb_client_3 import InfluxDBClient3, Point
from datetime import datetime

# Connection parameters
HOST = "http://127.0.0.1:8181"
TOKEN = None          # Replace with your InfluxDB 3 Core API token
ORG = None              # Replace with your organization name
DATABASE = "test_db"        # Bucket / database name

# Initialize client
client = InfluxDBClient3(host=HOST, token=TOKEN, org=ORG, database=DATABASE)

# --- WRITE TEST DATA ---
point = Point("test_measurement") \
    .tag("location", "lab") \
    .field("temperature", 22.5) \
    .time(datetime.utcnow())

client.write(point)
print("✅ Wrote test data to InfluxDB.")

# --- QUERY TEST DATA ---
query = """
SELECT * FROM test_measurement
WHERE time > now() - interval '5 minute'
LIMIT 5
"""

print("\n🔍 Query result:")
for record in client.query(query):
    print(record)

client.close()
