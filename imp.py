import os
import json

# Directory containing images
image_dir = "./"  # or your specific folder path
thumb_dir = "thumb"
output_file = "output.json"
fixed_r = "1720x3728"

# Collect entries
entries = []
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):
        base_name = os.path.splitext(filename)[0]
        parts = base_name.split("_")
        if len(parts) >= 2:
            name = f"{parts[0]} {parts[1]}"
        else:
            name = base_name

        entry = {
            "n": name,
            "url": filename,
            "t": os.path.join(thumb_dir, filename),
            "r": fixed_r
        }
        entries.append(entry)

# Save to JSON
with open(output_file, "w") as f:
    json.dump(entries, f, indent=2)

print(f"Saved {len(entries)} entries to {output_file}")