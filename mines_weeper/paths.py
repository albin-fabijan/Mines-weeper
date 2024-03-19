import os


class Paths:
    def __init__(self):
        self.root = self.define_root_directory()
        self.sprites = self.define_sprites_directory()

    def define_root_directory(self):
        current_file = os.path.abspath(__file__)
        root = os.path.join(
            current_file,
            os.pardir,
            os.pardir
        )
        absolute_root = os.path.abspath(root)
        return absolute_root

    def define_sprites_directory(self):
        sprites = os.path.join(
            self.root,
            "sprites"
        )
        absolute_sprites = os.path.abspath(sprites)
        return absolute_sprites

    def select_sprite(self, sprite_file_name):
        sprite_path = os.path.join(
            self.sprites,
            sprite_file_name
        )
        absolute_sprite = os.path.abspath(sprite_path)
        return absolute_sprite