# API-Integration-and-Data-Visualization

**Company** - CODETECH IT SOLUTIONS

**Name** - Tanmoy Das

**Intern ID** - CT06DR1738

**Domain** - Python Programming

**Duration** - 6 weeks

**Mentor** - Neela Santosh

This Python script is a simple yet powerful weather dashboard that shows the current weather of a city, in this case, Kolkata. It fetches real-time weather data using the OpenWeatherMap API and presents it in a visually appealing way with charts and graphs. Essentially, it’s a combination of data collection, organization, and visualization, all in one program.

**Tools and Libraries Used**

The script makes use of some of Python’s most popular libraries -

* **Requests** - This library is used to interact with the OpenWeatherMap API. By sending an HTTP GET request, it retrieves weather data for the city we specify. The API key ensures authorized access, and the request can be customized to return temperatures in Celsius, wind speed in meters per second, and other metrics.

* **Pandas** - Once we have the data, we use Pandas to organize it. Pandas is perfect for working with structured data, and it makes it easy to put the weather metrics—like temperature, humidity, pressure, and wind speed—into a neat table format called a DataFrame. This structured format is ideal for visualization.

* **Matplotlib** - This is a fundamental Python library for creating all sorts of plots. Here, it is used to set up a dashboard with four subplots in a 2x2 grid. Matplotlib handles things like figure layout, titles, and axes, giving us fine control over how everything looks.

* **Seaborn** - Built on top of Matplotlib, Seaborn makes plots more visually appealing with attractive color palettes and themes. In this script, it’s used to create a bar plot for the main weather metrics, making it easier to compare them at a glance.

**How the Script Works**

* **Fetching the Weather Data** - First, the script constructs a URL with the city name and API key and sends a request to the OpenWeatherMap API. It checks if the request was successful, and if not, it prints an error message. If everything is okay, it retrieves the data in JSON format.

* **Extracting Useful Information** - From the JSON response, the script extracts the key weather information:

  * weather_main - a general description like “Clear” or “Clouds”

  *weather_desc - a more detailed description of the weather

  *temp - current temperature in Celsius

  *humidity - the percentage of humidity in the air

  *pressure - atmospheric pressure in hPa

  *wind_speed - wind speed in meters per second

These values are then placed into a Pandas DataFrame, which makes them easy to work with for plotting.

**Visualizing the Data** -

**The dashboard has three sections** -

* **Bar Plot** - Shows the main metrics (temperature, humidity, pressure, wind speed) for easy comparison.

* **Pie Chart** - Compares humidity and wind speed visually, which adds a bit of fun to the dashboard.

* **Placeholder Section** - A simple text message indicating that more visualizations can be added in the future, like weather forecasts or trends.

Seaborn gives the plots a clean look with the “whitegrid” style, and Matplotlib organizes everything into the grid layout with proper titles.

**Real-Life Applications**

This kind of dashboard is not just a fun project—it has practical uses too. For example -

* **Personal Use** - People can check the weather of their city quickly before heading out.

* **Agriculture** - Farmers can monitor humidity, temperature, and wind to make better decisions about irrigation, spraying pesticides, or harvesting crops.

* **Smart Homes** - A home automation system could use this data to adjust heating, cooling, or ventilation.

* **Travel Planning** - Travelers can see current conditions to plan outdoor activities.

* **Learning Tool** - It’s a great example for students to learn how to work with APIs, handle data, and visualize it effectively.

**Conclusion**

In short, this script takes raw weather data from an API and turns it into a simple, readable, and visually appealing dashboard. By combining Requests, Pandas, Matplotlib, and Seaborn, it shows how programming can make complex data easy to understand. With a few modifications, it could be extended to include multi-city comparisons, forecasts, or historical trends, making it even more practical in real-world applications.


**Output** -

<img width="1169" height="799" alt="Image" src="https://github.com/user-attachments/assets/7233b8ed-03f4-4af8-a926-7fcf526877bc" />
