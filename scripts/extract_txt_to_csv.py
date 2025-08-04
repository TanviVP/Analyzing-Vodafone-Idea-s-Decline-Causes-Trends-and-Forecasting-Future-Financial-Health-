import os
import re
import pandas as pd
from tkinter import Tk, filedialog

# Input and output paths
input_dir = "../data/Raw datasets(Unprocessed)/converted_txt"
output_file = "../scripts/quarterly_kpis_expanded.xlsx"

# Ensure output directory exists
output_dir = os.path.dirname(output_file)
os.makedirs(output_dir, exist_ok=True)

# Define patterns for expanded KPIs
kpi_patterns = {
    "Revenue from Operations": r"Revenue\s+from\s+Operations.*?₹?\s*([\d,\.]+)",
    "EBITDA": r"EBITDA.*?₹?\s*([\d,\.]+)",
    "Net Profit": r"(?:Loss|Profit)\s+after\s+Tax.*?₹?\s*([\d,\.]+)",
    "ARPU": r"ARPU\s*\(?(?:Rs)?\)?\s*[^\d]{0,10}₹?\s*([\d,\.]+)",
    "CapEx": r"CapEx\s*(?:was)?\s*₹?\s*([\d,\.]+)",

    "Subscribers (Total)": r"Subscriber\s*base.*?([\d,\.]+)\s*million",
    "Subscribers (4G)": r"4G\s+subscriber\s+base.*?([\d,\.]+)\s*million",
    "Churn Rate": r"Churn\s*Rate\s*[:\-]?\s*([\d\.]+)%",
    
    "Minutes of Use": r"Minutes\s+of\s+Use\s*\(MoU\)\s*.*?([\d,\.]+)\s*minutes",
    "Total Data Usage": r"Total\s+Data\s+Traffic.*?([\d,\.]+\s*(?:PB|GB|TB))",
}

# Function to clean numeric values
def clean_number(text):
    return float(text.replace(",", "").strip())

records = []

# Prompt user to select folder containing TXT files
root = Tk()
root.withdraw()
try:
    input_dir = filedialog.askdirectory(title="Select folder containing TXT files")
finally:
    root.destroy()

if not input_dir:
    print("No folder selected. Exiting.")
    exit()

# Loop through .txt files
for file in sorted(os.listdir(input_dir)):
    if file.endswith(".txt"):
        quarter = file.replace(".txt", "")
        path = os.path.join(input_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        row = {"Quarter": quarter}

        for kpi, pattern in kpi_patterns.items():
            match = re.search(pattern, content, flags=re.IGNORECASE)
            if match:
                val = match.group(1)
                try:
                    if "million" in val.lower():
                        row[kpi] = float(val.lower().replace("million", "").strip())
                    elif "PB" in val or "GB" in val or "TB" in val:
                        row[kpi] = val.strip()
                    elif "%" in val:
                        row[kpi] = float(val.replace("%", "").strip())
                    else:
                        row[kpi] = clean_number(val)
                except:
                    row[kpi] = val
            else:
                row[kpi] = None

        records.append(row)
        print(f" Extracted from: {file}")

# Save output
df = pd.DataFrame(records)
df.to_excel(output_file, index=False)
print(f"\n Saved expanded KPI data to: {output_file}")
print(f"\n Saved expanded KPI data to: {output_file}")
