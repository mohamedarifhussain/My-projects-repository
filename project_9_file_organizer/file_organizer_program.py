import os
print("Welcome to file organizer!\n")
print("""You can organize different types of files 
into required folders\n""")
file_path = input('Enter the file path: ')
os.chdir(file_path)
print(os.getcwd())
print(os.listdir())

# files = os.listdir()
# print(files)
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
#
# print(os.listdir())
