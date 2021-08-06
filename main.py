import os
files = os.listdir()
txt_files = []
for file in files:
    if os.path.isfile(os.path.join(file)) and file.endswith('.txt'):
        txt_files.append(file)
        txt_files = sorted(txt_files)
        txt_files = txt_files[::-1]
file_number = 0
creating_a_file = []
for file in txt_files:
    file_number += 1
    writing_files = open(file, "r", encoding="UTF-8")
    creating_a_file += [file]
    creating_a_file += [str(file_number)]
    for writing_file in writing_files:
        creating_a_file += [writing_file.strip()]
new_file = open(r"C:\Users\vv\Desktop\working_with_files\New_file\New_file.txt", "w", encoding="UTF-8")
creating_a_file = '\n'.join(creating_a_file)
new_file.write(creating_a_file)



