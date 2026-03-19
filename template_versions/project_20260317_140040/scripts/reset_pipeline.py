import os
import shutil

# Carpetas de datos
folders = [
    "data/silver",
    "data/gold"
]

# Archivos obsoletos
obsolete_files = [
    "data/silver/personas_clean.csv",
    "data/gold/personas_summary.csv"
]

print("🧹 Cleaning old pipeline artifacts...")

for file in obsolete_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"❌ Removed {file}")

# limpiar silver y gold
for folder in folders:
    if os.path.exists(folder):
        for f in os.listdir(folder):
            path = os.path.join(folder, f)
            os.remove(path)
            print(f"🗑 Removed {path}")

print("✅ Pipeline cleaned")