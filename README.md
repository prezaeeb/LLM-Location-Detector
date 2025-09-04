# LLM-Location-Detector

<h3>Project Description</h3>

This project demonstrates the practical application of **LLMs** and **APIs** to solve a real-world problem. Using Python, the script communicates with a generative AI model to intelligently extract a specific location from a natural language query. It leverages **JSON** to receive the structured geospatial data, which is then used by the **Folium library for geospatial data visualization**. The final output is an interactive map that accurately plots the location, showcasing the power of combining AI with data visualization techniques.


<h3>Code Description</h3>
This Python script demonstrates how to leverage a large language model (LLM) to extract a specific geographic location from a text query and then plot that location on an interactive map. It combines the power of AI with a practical data visualization tool to turn a simple text prompt into a useful map.

<h3>Prerequisites</h3>
- To run this script, you will need the following Python libraries. You can install them by running the command below.

    -requests: Used to make HTTP requests to the LLM API.
    
    -folium: A powerful library for visualizing geospatial data on an interactive map.


<h3>Installation</h3>
- You can install the required libraries using pip:

    - pip install requests folium

    
<h3>How It Works</h3>
The script operates in two main parts:
  
  -**LLM API Call:** The script sends a user_query (e.g., "I'd like to find the location of the Brandenburg Gate in Berlin.") to the LLM. 
     It includes a system_instruction that explicitly tells the model to act as a geographic assistant and to return a structured JSON object with the location name, latitude, and longitude. 
     It also uses Google Search grounding to ensure the model finds accurate, up-to-date coordinates. The generationConfig is set to application/json to guarantee the response is in the desired format.

  -**Map Visualization:**  After a successful API call, the script parses the JSON response to extract the location data.
    It then uses the folium library to create an interactive map centered on the extracted latitude and longitude.
    A marker is placed at the exact location, complete with a tooltip and popup showing the name of the place.
    The final map is saved as an HTML file.

<h3>Usage</h3>

1. Save the script: Save the code provided in the location_detector.py file.

2. Install dependencies: Follow the installation steps above.

3. Run the script: Execute the script from your terminal.

        -python location_detector.py
