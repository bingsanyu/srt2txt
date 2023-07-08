import os
import glob
import re
import tkinter as tk
from tkinter import filedialog
try:
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    os.chdir(folder_selected)

    for file in glob.glob("*.srt"):
        with open(file, "r", encoding="utf-8") as f:
            lines = f.read()

        text = ''

        for line in lines.split("\n"):
            if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                line = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', line)
                text += '\n' + line.rstrip('\n')
            text = text.lstrip()

        with open(file + ".txt", "w") as f:
            f.write(text)

    os.startfile(folder_selected)
except:
    pass