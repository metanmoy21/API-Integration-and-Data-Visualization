import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIG ---
API_KEY = "fd98d6a5b03ba5b12248fa90faeab10a"    
CITY = "Kolkata"

# --- FETCH DATA ---
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Check for errors
if response.status_code != 200:
    print(f"Error fetching data: {data.get('message', 'Unknown error')}")
    exit()

# --- PARSE DATA ---
# Extract main weather info
weather_main = data['weather'][0]['main']
weather_desc = data['weather'][0]['description']
temp = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']

# Create a DataFrame for visualization
df = pd.DataFrame({
    'Parameter': ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Wind Speed (m/s)'],
    'Value': [temp, humidity, pressure, wind_speed]
})

# --- VISUALISATION ---

# Set seaborn style
sns.set(style="whitegrid")

# Create a figure with subplots (2 rows x 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle(f"Weather Dashboard for {CITY}", fontsize=16)

# 1. Barplot of weather parameters
sns.barplot(x='Parameter', y='Value', data=df, ax=axs[0, 0], palette='viridis')
axs[0, 0].set_title('Current Weather Metrics')
axs[0, 0].set_ylim(0, max(df['Value']) * 1.2)

# 2. Display weather main and description as text
axs[0, 1].axis('off')  # Hide axes
text = f"Weather: {weather_main}\nDescription: {weather_desc.capitalize()}"
axs[0, 1].text(0.5, 0.5, text, fontsize=14, ha='center', va='center')

# 3. Pie chart of humidity and wind contribution (just for fun)
labels = ['Humidity', 'Wind Speed']
sizes = [humidity, wind_speed]
axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgreen'], startangle=140)
axs[1, 0].set_title('Humidity vs Wind Speed')

# 4. Empty plot or you can add future data
axs[1, 1].axis('off')
axs[1, 1].text(0.5, 0.5, 'More visualizations coming soon...', ha='center', va='center', fontsize=12, style='italic')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
