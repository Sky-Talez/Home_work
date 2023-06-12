import sys
from pathlib import Path
import shutil
from Normalise import translate


CATEGORIES = {"Images" : [".jpeg", ".png", ".jpg", ".svg"],
              "Audio" : [".mp3", ".ogg", ".wav", ".amr"],
              "Video": [".mp4", ".mov", ".mkv", ".avi"],
              "Docs" : [".docx", ".doc", ".txt", ".pdf", ".csv", ".xlsx", ".pptx"],
              "Archives" : [ ".zip", ".gz", ".tar"]}

def move_file(file: Path, path : Path, cat : str):
    target_dir = path.joinpath(cat)
    if not target_dir.exists():
        target_dir.mkdir()
    file.replace(target_dir.joinpath(f"{translate(file.stem)} {file.suffix}"))


def get_categorie(file : Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def sort_folder(path: Path ):
    for i in path.glob("**/*"):
        if i.is_file:
            cat = get_categorie(i)
            move_file(i, path, cat)

def unpack_archives(path: Path):
    for i in path.iterdir():
        archive_dir = path.joinpath(i.stem)
        archive_dir.mkdir
        new_path = str(archive_dir)
        shutil.unpack_archive(i, new_path)
        i.unlink

def delete_empty_folders(path: Path):
    for i in path.glob("**/*"):
        if i.is_dir() and not any(i.iterdir()):
            i.rmdir()

def main(folder :str):
    
    path = Path(folder) 
    
    if not path.exists:
        return "folder not found"
    
    sort_folder(path)
    delete_empty_folders(path)
    archive_path = path.joinpath("Archives")
    if archive_path.exists:
        unpack_archives(archive_path)
    return "All ok"



if __name__ == "__main__":
    try:
        print(main(sys.argv[1]))
    except IndexError:
        print("No argument")