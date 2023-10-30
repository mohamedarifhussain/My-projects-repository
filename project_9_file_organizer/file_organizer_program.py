import os

print("Welcome to file organizer!\n")

print("""You can organize different types of files 
into required folders\n""")

file_path = input('Enter the file path: ')

os.chdir(file_path)

print(f"current working directory: {os.getcwd()}")

files_of_organizer = os.listdir(r"C:\Users\USER\Documents\Python Scripts\PythonProjects\project_9_file_organizer\file organizer")

files = os.listdir()
print(f"Current working directory's folders: {files}")
print(f"files_of_organizer (files): {files_of_organizer}")


# #TODO-1: The below code is a new method to for organize file.

for file in files:
    type_of_file = file[file.index('.')+1:]
    if type_of_file not in files_of_organizer:
        os.makedirs(f"C:\\Users\\USER\Documents\\Python Scripts\\PythonProjects\\project_9_file_organizer\\file organizer\\" + type_of_file)
    destination = "C:\\Users\\USER\\Documents\\Python Scripts\\PythonProjects\\project_9_file_organizer\\file organizer\\" + type_of_file

    os.rename(src=file_path+file, dst=destination+'\\'+file)

# #TODO-2: The below code is a different method to organize file so ignore it.
# for i in files:
#     if '.' in i:
#         index = i.index('.')
#         file_format = i[index+1:]
#         destination = ''
#         if file_format == 'txt':
#             destination = r"C:\Users\USER\Documents\Python Scripts\PythonProjects\project_9_file_organizer\file organizer\TEXT_FILES"
#         elif file_format == 'jpg':
#             destination = (r"C:\Users\USER\Documents\Python Scripts\PythonProjects\project_9_file_organizer\file organizer\JPEG_FILES")
#         elif file_format == 'pptx':
#             destination = (r"C:\Users\USER\Documents\Python Scripts\PythonProjects\project_9_file_organizer\file organizer\PPTX_FILES")
#         elif file_format == 'html':
#             destination = (r"C:\Users\USER\Documents\Python Scripts\PythonProjects\project_9_file_organizer\file organizer\HTML_FILES")
#         if destination != '':
#             os.rename(src=file_path+'\\'+i, dst=destination+'\\'+i)
#
#
# # os.rename(r"C:\Users\USER\Documents\file organizer\SAMPLE.txt", r"C:\Users\USER\Pictures\SAMPLE.txt")