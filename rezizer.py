from PIL import Image
import os

def rezize(path, percentage):
    files = os.listdir(path)
    try:
        os.makedirs(path + os.sep + "modified")
    except:
        print("Could not create directory")
    for file_str in files:
        if file_str.lower().endswith(".jpg"):
            img = Image.open(path + os.sep + file_str)
            size = img.size
            newsize = (int(size[0]*percentage), int(size[1]*percentage))
            resized_img = img.resize(newsize)
            exif = img.getexif()
            resized_img.save(path +  os.sep + "modified" + os.sep + file_str[0:-4] + 'modified' + ".jpg", exif=exif)
            print(f"Picture {files.index(file_str) + 1}")
            img.close()
    print("Images resized")



if __name__ == '__main__':
    rezize(os.getcwd(), .75)

