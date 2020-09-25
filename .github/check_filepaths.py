"""
Check that all Lessons have matching Practices & Keys

Usage:
    python check_filepaths.py
"""
import itertools
import os


def main():
    file_map = {
        "Practices/Practice": get_notebooks("Practices"),
        "Lessons/_Keys/KEY_Lesson": get_notebooks("Lessons/_Keys"),
        "Practices/_Keys/KEY_Practice": get_notebooks("Practices/_Keys"),
    }
    is_correct_all = True
    for lesson_file in sorted(get_notebooks("Lessons")):
        is_correct_lesson = True
        if not lesson_file.startswith("Lessons/Lesson"):
            raise ValueError(
                f"🚫 Error: Lesson filename `{lesson_file}` doesn't start with 'Lesson'."
            )
        suffix = lesson_file.strip("Lessons/Lesson")
        for prefix, files in file_map.items():
            expected_file = f"{prefix}{suffix}"
            if expected_file not in files:
                is_correct_lesson = False
                print(f"🚫 Error: Expected `{expected_file}` but file not found.")
            else:
                files.discard(expected_file)
        if is_correct_lesson:
            print(f"✅ {lesson_file}")
        else:
            is_correct_all = False

    unmatched_files = sorted(itertools.chain.from_iterable(file_map.values()))
    if unmatched_files:
        print("⚠️  Warning: detected files without matching lessons:")
        for file in unmatched_files:
            print("    ", file)
    if is_correct_all:
        print("🙌🏻 All lesson notebooks have corresponding practices & keys!")
    else:
        raise FileNotFoundError("🚫 File(s) not found; look above for expected paths.")

def get_notebooks(directory):
    return {os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".ipynb")}


if __name__ == "__main__":
    main()
