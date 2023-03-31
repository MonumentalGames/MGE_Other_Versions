import pygame
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as PIL_Image
from screeninfo import get_monitors

#from .Global_Cache import Cache
from .Camera import Camera
from .Platform import Platform

mode_flags = {"NOFRAME": 32, "RESIZABLE": 16, "FULLSCREEN": -2147483648}

class Screen:
    def __init__(self, opengl: bool = False):
        self.__Window_Type__ = "main"

        if opengl:
            self.screen = pygame.display.set_mode((1, 1), 1073741824 | 2)
            glViewport(0, 0, 1, 1)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        else:
            if Platform.system == "Android":
                self.screen = pygame.display.set_mode((0, 0))
            else:
                self.screen = pygame.display.set_mode((1, 1), 32)

        self.monitor_resolution = [get_monitors()[0].width, get_monitors()[0].height]

        self.object_draw_list = []

        self.opengl = opengl
        self.render_all_objects = True
        self.clock = pygame.time.Clock()
        self.camera = Camera()

    def clear_screen(self):
        if self.opengl:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glClearDepth(1.0)
        else:
            self.screen.fill((0, 0, 0))

    def fill(self, color):
        if self.opengl:
            glClearColor(round((color[0] / 255 * 100) / 100, 4), round((color[1] / 255 * 100) / 100, 4), round((color[2] / 255 * 100) / 100, 4), 1)
            glClear(GL_COLOR_BUFFER_BIT)
        else:
            self.screen.fill(color)

    def get_screen_img(self):
        if not self.opengl:
            image = self.screen
            image_size = self.get_size()
            raw_str = pygame.image.tostring(pygame.transform.scale(image, image_size), "RGB", False)
            return PIL_Image.frombytes("RGB", image_size, raw_str)

    def get_size(self):
        if self.opengl:
            size = [*numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))]
            return [size[2], size[3]]
        else:
            return self.screen.get_size()

    def set_size(self, x: int, y: int, mode: str = "", opengl: bool = False):
        self.opengl = opengl
        flag = mode_flags.get(mode.upper(), 0)
        if opengl:
            self.screen = pygame.display.set_mode((x, y), 1073741824 | 2 | flag)
            glViewport(0, 0, x, y)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        else:
            self.screen = pygame.display.set_mode((x, y), flag)
        self.render_all_objects = True
