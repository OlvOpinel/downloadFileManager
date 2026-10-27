import time
import shutil
from pathlib import Path

download = Path("/chemin")

DESTINATIONS = {
    ".png": download / "photos",
    ".jpg": download / "photos",
    ".jpeg": download / "photos",
    ".pdf": download / "pdfs",
    ".zip": download / "archives",
    ".gif": download / "gifs",
    ".docx": download / "docxs"
}

for folder in DESTINATIONS.values():
    folder.mkdir(exist_ok=True)

print("Surveillance par vérification active démarrée...")

while True:
    try:
        for files in download.glob("*"):
            if files.is_file():
                ext = files.suffix.lower()
            
                if ext in DESTINATIONS:
                    time.sleep(1)
                    
                    shutil.move(str(files), str(DESTINATIONS[ext] / files.name))
                    print(f"Fichier {files.name} déplacé dans {DESTINATIONS[ext]}")
                    
    except Exception as e:
        print(f"Erreur : {e}")
        
    time.sleep(5)

