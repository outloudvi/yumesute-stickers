import UnityPy
import os

files = filter(lambda x:x.endswith(".bundle"),os.listdir("."))
for filename in files:
    up = UnityPy.load(filename)
    tx2d = filter(lambda x: x.type.name == "Texture2D", up.objects).__next__()
    tx2d.read().image.save(filename.split(".")[0] + ".png")
    print(f"Finishing {filename}")