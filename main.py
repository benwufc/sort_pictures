import os
import exifread
path = "/home/ben/Pictures/2018-02-16_Thailand_travel_HuaHin_LetsSeaResort"
pic_list = []
pic_timestamp = []
video_list = []
for file_name in os.listdir(path):
    if "JPG" in file_name:
        pic_list.append(file_name)
        f = open(path + '/' + file_name, 'rb')
        time_tags = '%s' % exifread.process_file(f)["EXIF DateTimeOriginal"]
        pic_timestamp.append(time_tags)
    elif "mov" in file_name:
        video_list.append(file_name)


for idx, (time, file_name) in enumerate(sorted(zip(pic_timestamp, pic_list))):
    os.rename(path + '/' + file_name, path + '/LetsSeaResort_'+ str(idx))
    
