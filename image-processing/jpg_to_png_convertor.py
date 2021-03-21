import os
import shutil
import sys

from PIL import Image


class SameDirError(Exception):
    def __init__(self):
        super().__init__('Source and Destination directory should not be same')


class JpgToPngConverter:

    def __init__(self, dir_path, new_path):
        self.dir_path = dir_path
        self.new_path = new_path
        self.num_of_files_converted = 0
        self.create_dir()
        self.convert_images()

    def create_dir(self):
        if os.path.exists(self.new_path):
            shutil.rmtree(self.new_path)
        os.makedirs(self.new_path)

    def convert_images(self):
        try:
            dir_info = os.listdir(self.dir_path)
            if dir_info:
                for filename in dir_info:
                    if filename.endswith('jpg'):
                        img = Image.open(os.path.join(self.dir_path, filename))
                        img.save(os.path.join(self.new_path, filename.split('.')[0] + '.png'))
                        self.num_of_files_converted += 1
                if self.num_of_files_converted == 0:
                    print('No JPG file found in the source folder for conversion')
                else:
                    print(f'Number of files converted from JPG to PNG is {str(self.num_of_files_converted)}')
            else:
                print('Source Directory is empty')
        except FileNotFoundError:
            print("Source folder not found. Kindly provide the correct path")
            shutil.rmtree(self.new_path)


if __name__ == '__main__':
    try:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        if source_dir == dest_dir:
            raise SameDirError
        convertor = JpgToPngConverter(source_dir, dest_dir)
    except IndexError as err:
        print("Please provide source path and destination path for successful conversion")
    except SameDirError as err:
        print(err)
