from datetime import datetime

# Current time in ISO 8601 format
iso_format = datetime.now().isoformat()
print(iso_format)  # Example: '2024-06-22T13:49:08.123456'

# Custom format
custom_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(custom_format)  # Example: '2024-06-22 13:49:08'
