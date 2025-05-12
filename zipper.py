# zipper.py

import zipfile

with zipfile.ZipFile("charts.zip", "w") as zipf:
    zipf.write("chart.png")

print("Dummy chart zipped.")
