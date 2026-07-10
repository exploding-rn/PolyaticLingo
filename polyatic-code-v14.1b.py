import csv
import shutil
import sys
from datetime import datetime
from pathlib import Path
import tkinter as tk

# --- Cipher setup: only letters ---
POLYATIC_SEED = " zxcvbnmlkjhgfdsaqwertyuiop "
BACKWARDS = POLYATIC_SEED[::-1]
CODE = {POLYATIC_SEED[i]: BACKWARDS[i] for i in range(len(POLYATIC_SEED))}
TRANSLATION_TABLE = {ord(char): CODE[char] for char in CODE if char.isalpha()}
DATA_FILE_NAME = "codes.csv"


def get_data_file_path():
    if getattr(sys, "frozen", False):
        bundled_path = Path(getattr(sys, "_MEIPASS", "")) / DATA_FILE_NAME
        if bundled_path.exists():
            target_dir = Path.home() / "AppData" / "Local" / "PolyaticTranslator"
            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / DATA_FILE_NAME
            if not target_path.exists():
                shutil.copy2(bundled_path, target_path)
            return target_path

        exe_dir = Path(sys.executable).resolve().parent
        candidate = exe_dir / DATA_FILE_NAME
        if candidate.exists():
            return candidate

    return Path(__file__).resolve().parent / DATA_FILE_NAME


CSV_FILE = get_data_file_path()


def atbash(text):
    return text.lower().translate(TRANSLATION_TABLE)


def load_previous_translations():
    if not CSV_FILE.exists():
        return []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader if row]


def save_translation(original_text, translated_text):
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = CSV_FILE.exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp", "original", "translated"])
        if not file_exists or CSV_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "original": original_text,
            "translated": translated_text,
        })


def on_encode():
    original_text = entry.get()
    result = atbash(original_text)
    output_var.set(result)
    if original_text.strip():
        save_translation(original_text, result)


def on_copy():
    root.clipboard_clear()
    root.clipboard_append(output_var.get())
    root.update()


def show_previous_translations():
    previous = load_previous_translations()
    history_window = tk.Toplevel(root)
    history_window.title("Previous Translations")
    history_window.geometry("520x320")

    text_box = tk.Text(history_window, wrap="word", height=16, width=60)
    text_box.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(history_window, command=text_box.yview)
    scrollbar.pack(side="right", fill="y")
    text_box.config(yscrollcommand=scrollbar.set)
    text_box.config(state="normal")

    if previous:
        for item in previous:
            text_box.insert("end", f"{item['timestamp']}\n")
            text_box.insert("end", f"Input: {item['original']}\n")
            text_box.insert("end", f"Output: {item['translated']}\n\n")
    else:
        text_box.insert("end", "No previous translations yet.")

    text_box.config(state="disabled")


root = tk.Tk()
root.title("Polyatic Translator")
root.geometry("360x260")
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Apply the icon
try:
    icon_path = get_resource_path("a136f8d2.ico")
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Icon not found: {e}")
tk.Label(root, text="Text to Translate").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Translate", command=on_encode).pack(pady=5)

tk.Label(root, text="Result:").pack()
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, width=40, state="readonly")
output_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=on_copy).pack(pady=5)
tk.Button(root, text="View Previous Translations", command=show_previous_translations).pack(pady=5)

root.mainloop()
