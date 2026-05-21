
from pathlib import  Path
import shutil

folder_to_scan = Path("test_folder")

file_categories = {
	".pdf": "pdfs",
	".jpg": "images",
	".jpeg": "images",
	".png": "images",
	".docx": "documents",
	".txt": "texts"
}

for file_path in folder_to_scan.iterdir(): 
	if file_path.is_file():
		extension = file_path.suffix.lower()
		print(f"{file_path.name} -> {extension}")
  
