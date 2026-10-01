def format_location(latitude, longitude):
    # Pure logic: accepts data, processes/packs it, returns it
    return latitude, longitude

# --- Execution ---
# 1. Collect inputs outside
user_lat = float(input("Enter latitude: "))
user_lon = float(input("Enter longitude: "))

# 2. Pass variables into the function and unpack the return
lat, lon = format_location(user_lat, user_lon)
print(f"Latitude: {lat}, Longitude: {lon}")