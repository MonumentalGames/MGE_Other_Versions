import pygame
from .Key_Maps import Key_Map

def keyboard(key):
    key = str(key).lower()
    event_key = pygame.key.get_pressed()

    if key == "all":
        if True in event_key:
            press_keys = []
            for key_cache in Key_Map.keys():
                if key_cache != "all":
                    if isinstance(Key_Map[key_cache]["key"], int):
                        if event_key[Key_Map[key_cache]["key"]]:
                            press_keys.append(key_cache)
            if press_keys:
                return press_keys
            return True

    if key in Key_Map:
        if isinstance(Key_Map[key]["key"], int):
            return event_key[Key_Map[key]["key"]]
        else:
            return any(event_key[k] for k in Key_Map[key]["key"])

    return False
