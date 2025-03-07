# 1. --------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT DATE(timestamp) AS attack_date, COUNT(*) AS attack_count FROM attack_logs GROUP BY attack_date ORDER BY attack_date;")
data = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Date', 'Attacks'])

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Attacks'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Number of Attacks")
plt.title("Attack Trends Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Close connection
cursor.close()
conn.close()


# 2. ------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT attack_type, COUNT(*) FROM attack_logs GROUP BY attack_type;")
data = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Attack Type', 'Count'])

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['Count'], labels=df['Attack Type'], autopct='%1.1f%%', startangle=140)
plt.title("Attack Type Distribution", pad=20)  # Adds spacing for title

# Adjust layout to prevent overlap
plt.tight_layout()  # Ensures proper spacing
plt.subplots_adjust(bottom=0.2)  # Adds space at the bottom

# Show plot
plt.show()

# Close connection
cursor.close()
conn.close()

# 3. --------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

cursor.execute("SELECT severity_level, COUNT(*) FROM attack_logs GROUP BY severity_level ORDER BY FIELD(severity_level, 'Low', 'Medium', 'High', 'Critical');")
data = cursor.fetchall()

df = pd.DataFrame(data, columns=['Severity Level', 'Count'])

# Bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x=df['Severity Level'], y=df['Count'], palette=['green', 'yellow', 'orange', 'red'])
plt.xlabel("Severity Level")
plt.ylabel("Number of Attacks")
plt.title("Severity Levels of Attacks")
plt.show()

cursor.close()
conn.close()

# 4. ---------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

cursor.execute("SELECT firewall_action, COUNT(*) FROM attack_logs GROUP BY firewall_action;")
data = cursor.fetchall()

df = pd.DataFrame(data, columns=['Firewall Action', 'Count'])

# Plot
plt.figure(figsize=(6, 5))
plt.bar(df['Firewall Action'], df['Count'], color=['blue', 'orange', 'red'])
plt.xlabel("Firewall Action")
plt.ylabel("Count")
plt.title("Firewall Actions Taken")
plt.show()

cursor.close()
conn.close()

# 5. --------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

cursor.execute("SELECT affected_device_id, COUNT(*) FROM attack_logs GROUP BY affected_device_id ORDER BY COUNT(*) DESC LIMIT 10;")
data = cursor.fetchall()

df = pd.DataFrame(data, columns=['Device ID', 'Attack Count'])

# Horizontal bar plot
plt.figure(figsize=(8, 6))
plt.barh(df['Device ID'], df['Attack Count'], color='purple')
plt.xlabel("Number of Attacks")
plt.ylabel("Device ID")
plt.title("Top 10 Affected Devices")
plt.gca().invert_yaxis()
plt.show()

cursor.close()
conn.close()

# 6. ---------------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT responsible_team, AVG(response_time_minutes) FROM incident_response GROUP BY responsible_team;")
data = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Team', 'Avg Response Time'])

# Plot
plt.figure(figsize=(10, 6))  # Increased figure size
sns.barplot(x=df['Team'], y=df['Avg Response Time'], palette="coolwarm")

# Labels & Title
plt.xlabel("Response Team", fontsize=12)
plt.ylabel("Average Response Time (Minutes)", fontsize=12)
plt.title("Incident Response Team Performance", fontsize=14)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=30, ha='right')  # Rotates and aligns labels
plt.tight_layout()  # Adjusts layout to prevent cut-off

# Show plot
plt.show()

# Close connection
cursor.close()
conn.close()

# 7. ------------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(host="localhost", user="root", password="Keerthi@2503", database="cyber_security_2db")
cursor = conn.cursor()

cursor.execute("SELECT d.location, COUNT(a.attack_id) FROM attack_logs a JOIN devices d ON a.affected_device_id = d.device_id GROUP BY d.location;")
data = cursor.fetchall()

df = pd.DataFrame(data, columns=['Location', 'Attack Count'])

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Location'], y=df['Attack Count'], size=df['Attack Count'], sizes=(50, 300), hue=df['Attack Count'], palette="coolwarm")
plt.xlabel("Location")
plt.ylabel("Number of Attacks")
plt.title("Attack Sources by Location")
plt.xticks(rotation=45)
plt.show()

cursor.close()
conn.close()
