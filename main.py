# UTF-8, @author: punarvas
import os
import shutil

path = "D:\\vehicle detection dataset\\data_object_label_2\\training\\label_2"
source = "D:\\vehicle detection dataset\\KITTI\\training\\image_2"
dest = "C:\\Users\\Akash\\Desktop\\image data\\images\\ideal"

file_list = os.listdir(path)

files_to_select = []

for image_file in file_list:
    with open(os.path.join(path, image_file), "r") as file:
        lines = file.readlines()
        for line in lines:
            if "Car" in line:
                files_to_select.append(image_file)
                break
                
print(f"Found {len(files_to_select)} image(s) with Car")

file_list = list(map(lambda x: x.split(".")[0] + ".png\n", files_to_select))
with open("files.txt", "w", encoding = "utf-8") as result_file:
    for each_file in file_list:
        result_file.write(each_file)
    result_file.close()

for each_file in file_list:
    source_path = os.path.join(source, each_file.rstrip("\n"))
    dest_path = os.path.join(dest, each_file.rstrip("\n"))
    shutil.copyfile(source_path, dest_path)
    
print("Completed.")
