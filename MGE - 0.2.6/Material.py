import pygame
from PIL import ImageFilter

from .MGE import Program

class Material:
    def __init__(self, texture=None, color=(120, 120, 255), alpha=255):
        self.color = color
        self.alpha = alpha
        self.texture = texture
        self.Surface = pygame.Surface((16, 16))

        self.n_surf = 0
        self.surf_temp = 0

        self.object_render = False
        self.always_render = False

    def render(self, opengl: bool = False):
        if self.texture.image is not None:
            # Render Img
            cache_img = None
            if self.texture.image.type == "simple image":
                cache_img = self.texture.image.image
                if self.texture.blurr >= 1:
                    cache_img = cache_img.filter(ImageFilter.BoxBlur(self.texture.blurr))
                self.Surface = pygame.image.fromstring(cache_img.tobytes(), cache_img.size, cache_img.mode)
            # Render Gif
            elif self.texture.image.type == "gif":
                if self.surf_temp >= Program.get_fps() / self.texture.image.data_gif["fps"]:
                    if len(self.texture.image.data_gif["data"]) > 1:
                        if self.n_surf <= len(self.texture.image.data_gif["data"]) - 1:
                            cache_img = None
                            self.Surface = self.texture.image.data_gif["data"][self.n_surf]
                            self.n_surf += 1
                        else:
                            cache_img = None
                            self.Surface = self.texture.image.data_gif["data"][0]
                            self.n_surf = 1
                    else:
                        cache_img = None
                        self.Surface = pygame.Surface((16, 16))
                    self.surf_temp = 0
                self.surf_temp += 1
                self.always_render = True

            if opengl:
                self.texture.OpenGL_texture_update(self.Surface)
        # Render Sprite
        elif self.texture.sprite is not None:
            cache_img = self.texture.sprite.get_img_sprite()
            self.Surface = pygame.image.fromstring(cache_img.tobytes(), cache_img.size, cache_img.mode)

    def add_texture(self, texture):
        self.texture = texture

    def set_color(self, color):
        self.color = color

    def set_alpha(self, alpha):
        print(alpha)
        self.alpha = alpha

    def get_color(self):
        return self.color

    def get_alpha(self):
        return self.alpha

    def get_textures(self):
        return self.texture
