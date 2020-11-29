import os

image_files = []
os.chdir(os.path.join("data", "obj"))
print('list', os.listdir(os.getcwd()))
for dirname in os.listdir(os.getcwd()):
    for filename in os.listdir(dirname):
        if filename.endswith(".txt"):
            image_files.append("data/obj/" + dirname + "/" + filename[:-4] + ".jpg")
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
