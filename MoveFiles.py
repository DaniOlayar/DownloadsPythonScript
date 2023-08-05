import os
import shutil

source_dir = 'C:/Users/danie/Downloads'
pictures_destination = 'E:/Fotos'
documents_destination = 'E:/Documentos'
downloads_destination = 'E:/Descargas'
compressed_destination = 'E:/Comprimidos'

pictures_formats = ['.jpg', '.jpeg', '.png']
documents_formats = ['.doc', '.docx', '.pdf', '.xls', 'xlsx', '.ppt', 'pptx', '.txt']
downloads_formats = ['.msi', '.exe']
compressed_formats = ['.rar', '.zip']

def move_file_to_destination(source_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file_name = os.path.basename(source_path)
    destination_path = os.path.join(destination_folder, file_name)

    # If the file already exists in the destination directory, rename it
    index = 1
    while os.path.exists(destination_path):
        file_name, file_extension = os.path.splitext(file_name)
        new_file_name = f"{file_name} ({index}){file_extension}"
        destination_path = os.path.join(destination_folder, new_file_name)
        index += 1

    shutil.move(source_path, destination_path)

for file in os.listdir(source_dir):
    file_extension = os.path.splitext(file)[-1].lower()
    source_path = os.path.join(source_dir, file)

    if file_extension in pictures_formats:
        move_file_to_destination(source_path, pictures_destination)
    elif file_extension in documents_formats:
        move_file_to_destination(source_path, documents_destination)
    elif file_extension in compressed_formats:
        move_file_to_destination(source_path, downloads_destination)
    elif file_extension in downloads_formats:
        move_file_to_destination(source_path, downloads_destination)
