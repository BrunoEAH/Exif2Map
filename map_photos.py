import folium
import re

def map_coordinates(locations,txt_file):
    
    #Regex for latitude and longitude
    lat_pattern = re.compile(r"Composite:GPSLatitude:\s*([-+]?\d*\.\d+|\d+)")
    lon_pattern = re.compile(r"Composite:GPSLongitude:\s*([-+]?\d*\.\d+|\d+)")

    #Open metadata.txt
    with open(txt_file, "r") as file: 
        
        lines = file.readlines()
        
        lat, lon = None, None

        for line in lines:
            lat_match = lat_pattern.search(line)
            lon_match = lon_pattern.search(line)
            
            if lat_match:
                lat = float(lat_match.group(1))  # Extract latitude
            
            if lon_match:
                lon = float(lon_match.group(1))  # Extract longitude
            
            # Store location
            if lat is not None and lon is not None:
                locations.append((lat, lon))
                lat, lon = None, None  

    # Create a Folium map centered on the first coordinate
    if locations:
        map_center = locations[0]
        m = folium.Map(location=map_center, zoom_start=5)

        # Add markers for each extracted coordinate
        for lat, lon in locations:
            folium.Marker([lat, lon], popup=f"({lat}, {lon})").add_to(m)

        m.save("map.html")
        print("Map saved as 'map.html'. Open it in your browser.")
    else:
        print("No coordinates found in the file.")