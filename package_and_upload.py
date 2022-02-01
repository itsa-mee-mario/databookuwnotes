

import os
import sys

# move images to assets folder
os.system("mv *.png Assets")

# create index files
dir = "Notes"
files = os.listdir(dir)
for file in files:
    if file.endswith(".md"):
        file_name = file[:-3]
        file_path = os.path.join(dir, file)
        with open(file_path, "r") as f:
            content = f.read()
            content = content.split(".")[0]
            content = "[[" + content + "]]"
        with open(os.path.join(dir, file_name + "_index"), "w") as f:
            f.write(content)
            

