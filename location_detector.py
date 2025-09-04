#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A simple Python script to use an LLM to find a location and plot it on a map.
# This script requires the `requests` and `folium` libraries.
# You can install them by uncommenting and running the line below:
# pip install requests folium

import requests
import json
import folium
import sys

# Define your API key (leave as an empty string)
api_key = ""
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

# The text from which to extract the location.
user_query = "I'd like to find the location of the Brandenburg Gate in Berlin."

# System instruction to ensure the LLM returns a structured JSON object.
# The JSON schema must be exactly `{"location_name": "[name]", "latitude": [lat], "longitude": [lon]}`.
system_instruction = {
    "parts": [{
        "text": "You are a geographic assistant. Your task is to extract a single location from the provided text and return its name, latitude, and longitude as a JSON object. Use Google Search grounding to find the exact coordinates. If no location is found, return `null`."
    }]
}

# Construct the payload for the API request
payload = {
    "contents": [{
        "parts": [{
            "text": user_query
        }]
    }],
    "tools": [{
        "google_search": {}
    }],
    "systemInstruction": system_instruction,
    "generationConfig": {
        "responseMimeType": "application/json"
    }
}

print("Making API call to find location...")

# Make the API call
try:
    response = requests.post(api_url, json=payload)
    response.raise_for_status()
    result = response.json()

    # Extract the JSON string from the response
    json_string = result['candidates'][0]['content']['parts'][0]['text']
    location_data = json.loads(json_string)

    print("Location found:")
    print(json.dumps(location_data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
    location_data = None
except (KeyError, IndexError, json.JSONDecodeError) as e:
    print(f"Could not parse API response: {e}")
    print("Raw API response:", result)
    location_data = None
    
# --- Map Visualization ---
if location_data:
    try:
        # Extract the coordinates and name
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        location_name = location_data['location_name']

        # Create the map object, centered at the location
        m = folium.Map(location=[latitude, longitude], zoom_start=15)

        # Add a marker for the location
        folium.Marker(
            location=[latitude, longitude],
            popup=location_name,
            tooltip=location_name
        ).add_to(m)

        # Save the map to an HTML file and display the path
        output_file = f"{location_name.replace(' ', '_')}_map.html"
        m.save(output_file)
        print(f"\nInteractive map saved to: {output_file}")
        
    except KeyError as e:
        print(f"Could not find required key in location data: {e}", file=sys.stderr)
        print("Data received:", location_data, file=sys.stderr)
else:
    print("\nNo valid location data was found to create a map.")

