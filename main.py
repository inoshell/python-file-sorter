import os
import shutil

ext_to_folder = {
    '.jpg': r'G:\Sorted_Files\IMAGE',
    '.jpeg': r'G:\Sorted_Files\IMAGE',
    '.png': r'G:\Sorted_Files\IMAGE',
    '.gif': r'G:\Sorted_Files\IMAGE',
    '.bmp': r'G:\Sorted_Files\IMAGE',
    '.tif': r'G:\Sorted_Files\IMAGE',
    '.tiff': r'G:\Sorted_Files\IMAGE',
    '.doc': r'G:\Sorted_Files\DOCUMENTS',
    '.docx': r'G:\Sorted_Files\DOCUMENTS',
    '.txt': r'G:\Sorted_Files\DOCUMENTS',
    '.pdf': r'G:\Sorted_Files\DOCUMENTS',
    '.xls': r'G:\Sorted_Files\DOCUMENTS',
    '.xlsx': r'G:\Sorted_Files\DOCUMENTS',
    '.ppt': r'G:\Sorted_Files\DOCUMENTS',
    '.pptx': r'G:\Sorted_Files\DOCUMENTS',
    '.mp4': r'G:\Sorted_Files\VIDEO',
    '.mov': r'G:\Sorted_Files\VIDEO',
    '.avi': r'G:\Sorted_Files\VIDEO',
    '.mp3': r'G:\Sorted_Files\AUDIO',
    '.wav': r'G:\Sorted_Files\AUDIO',
    '.exe': r'G:\Sorted_Files\PROGRAMS',
}


name_to_count = {}
dir_path = r'D:'


for root, dirs, files in os.walk(dir_path):
    for filename in files:
        _, ext = os.path.splitext(filename)

        if ext in ext_to_folder:
            folder_name = ext_to_folder[ext]
            folder_path = os.path.join(root, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            new_filename = filename
            count = 1
            while new_filename in name_to_count:
                count += 1
                new_filename = f'{os.path.splitext(filename)[0]}_{count}{ext}'
            name_to_count[new_filename] = 1
            shutil.move(os.path.join(root, filename), os.path.join(folder_path, new_filename))
            print(os.path.join(root, filename) + " + " + os.path.join(folder_path, new_filename))
        else:
            print(f'Unsuitable file extension {os.path.join(root, filename)}')
