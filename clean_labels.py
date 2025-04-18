import os
import re
import pandas as pd

# Define the directory containing the audio files
CLEAN_DIR = "whale_audio_clean"
LABELS_PATH = os.path.join(CLEAN_DIR, "labels.csv")

# Function to clean the label
def clean_label(filename):
    # Remove non-alphanumeric characters (commas, parentheses, etc.)
    cleaned = re.sub(r'[^a-zA-Z0-9_ ]', '', filename)  # Keep alphanumeric characters and underscores/space
    
    # Replace multiple spaces or underscores with a single one
    cleaned = re.sub(r'[_\s]+', '_', cleaned)
    
    # Ensure it's in uppercase
    cleaned = cleaned.upper()

    # Extract species name by splitting at the first underscore
    label_parts = cleaned.split('_')
    if len(label_parts) >= 2:
        label = "_".join(label_parts[:2])  # Combine first two parts (e.g., "BELUGA_WHITE")
    else:
        label = cleaned  # In case of any strange formats, use the full name

    return label

# Prepare data for labeling
data = []

# Process all files in the directory
for filename in os.listdir(CLEAN_DIR):
    if filename.endswith(".wav"):
        label = clean_label(filename)
        data.append({"filename": filename, "label": label})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the cleaned labels as a CSV
df.to_csv(LABELS_PATH, index=False)

# Display some of the cleaned labels
df.head()
