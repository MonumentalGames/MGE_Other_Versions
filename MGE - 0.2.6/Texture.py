import pygame
from OpenGL.GL import *

class Texture:
    def __init__(self, image=None, sprite=None):
        if image is not None:
            if image.type == "simple image":
                self.image = image
            elif image.type == "gif":
                self.image = image
            self.sprite = None
        elif sprite is not None:
            self.sprite = sprite
            self.image = None
        self.opengl_texture = None
        self.blurr = 0

    def OpenGL_texture_update(self, image=None):
        #textureSurface = pygame.image.load(path)
        #pygame.image.tostring(textureSurface, "RGBA", 1)
        if image is None:
            image = pygame.image.fromstring(self.image.image.tobytes(), self.image.image.size, self.image.image.mode)
            textureData = pygame.image.tostring(image, "RGBA", 1)
        else:
            textureData = pygame.image.tostring(image, "RGBA", 1)
            #print(textureData)

        if self.opengl_texture is not None:
            glDeleteTextures(1, (self.opengl_texture,))

        width, height = self.image.size
        # glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        self.opengl_texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.opengl_texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glDisable(GL_TEXTURE_2D)

    def OpenGL_texture(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.opengl_texture)

    def set_image(self, image=None, sprite=None):
        if image is not None:
            if image.type == "simple image":
                self.image = image
            #elif image.type == "movie":
            #    self.image = image
            self.sprite = None
        elif sprite is not None:
            self.sprite = sprite
            self.image = None

    def set_blurr(self, blurr):
        self.blurr = blurr
