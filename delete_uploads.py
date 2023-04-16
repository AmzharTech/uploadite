import os

folder = 'static/uploads/'  # replace with the actual path to your uploads folder
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'{filename} deleted successfully')
    except Exception as e:
        print(f'Error in deleting {filename}: {e}')
