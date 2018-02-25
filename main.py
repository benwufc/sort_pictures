import os
import exifread
import time
import shutil
#===== adjusted parameter =====
path = "/home/benjamin/Pictures/"
folder = "test_folder"
file_header_name = "Thai_travel"
#==============================
PWD = os.path.join(path, folder)
EXTENSIONS = (".jpg", "jpeg", ".JPG", ".JPEG")

def get_exif_date(fn):
    f = open(os.path.join(PWD, fn),'rb')
    if os.path.splitext(fn)[-1] in EXTENSIONS:
        tags_time = "%s" % exifread.process_file(f)["EXIF DateTimeOriginal"]
        return tags_time.replace(":", "-")
    else:
        print "this file:", fn, " isn't jpg file."
    f.close()


pic_list = []

for fn in os.listdir(PWD):
    pic_time = get_exif_date(fn)
    pic_list.append((pic_time, fn))
for idx, (pic_time, fn) in enumerate(sorted(pic_list)):
    pic_day = pic_time[0:10]
    f_name_day = file_header_name + '_' + pic_day
    new_folder = os.path.join(path, f_name_day)
    original_file = os.path.join(PWD, fn)
    new_file_name = f_name_day + "_" + str(idx) 
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.copy(original_file, new_folder)
    os.rename(os.path.join(new_folder, fn), os.path.join(new_folder, new_file_name) )


