import shutil, os
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
os.makedirs("/output", exist_ok=True)
shutil.copyfile(src, "/output/entry.png")
