import os

image_files = []
os.chdir(os.path.join("data", "test"))
print('list', os.listdir(os.getcwd()))
for dirname in os.listdir(os.getcwd()):
    for filename in os.listdir(dirname):
        if filename.endswith(".jpg"):
            image_files.append("data/test/" + dirname + "/" + filename)
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")