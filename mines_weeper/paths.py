import os


current_file_path = os.path.abspath(__file__)
root_directory = os.path.join(current_file_path, os.pardir, os.pardir)
absolute_root_directory = os.path.abspath(root_directory)

sprite_directory = os.path.join(absolute_root_directory, "sprites")
absolute_sprite_directory = os.path.abspath(sprite_directory)


def select_sprite(sprite_file_name):
    sprite_path = os.path.join(absolute_sprite_directory, sprite_file_name)
    absolute_sprite_path = os.path.abspath(sprite_path)
    return absolute_sprite_path