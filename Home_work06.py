import sys
from pathlib import Path
import shutil
from Normalise import translate


CATEGORIES = {"images" : [".jpeg", ".png", ".jpg", ".svg"],
              "audio" : [".mp3", ".ogg", ".wav", ".amr"],
              "video": [".mp4", ".mov", ".mkv", ".avi"],
              "docs" : [".docx", ".doc", ".txt", ".pdf", ".csv", ".xlsx", ".pptx"],
              "archives" : [ ".zip", ".gz", ".tar"]}

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

def unpack_archive(path: Path):
    for i in path.iterdir():
        shutil.unpack_archive(i, path.joinpath(i.stem))

def delete_empty_folders(path: Path):
    for i in path.glob("**/*"):
        if i.is_dir():
            if len(i.iterdir) == 0:
                del i

def main(folder :str):
    try:
        path = Path(folder) 
    except IndexError:
        return "No argument"
    
    if not path.exists:
        return "folder not found"
    
    sort_folder(path)
    delete_empty_folders(path)
    archive_path = path.joinpath("archives")
    if archive_path.exists:
        unpack_archive(archive_path)
    return "All ok"



if __name__ == "__main__":
    print(main(sys.argv[1]))