# MGE Other Versions

Versions: ('0.2.0', 'Beta-0.2.1', 'Beta-0.2.6')  

## Dependencies
from 0.2.0 to 0.2.1  
[`pygame`](https://pypi.org/project/pygame/) -
[`numpy`](https://pypi.org/project/numpy/) -
[`pillow`](https://pypi.org/project/Pillow/) -
[`opencv-python`](https://pypi.org/project/opencv-python/) -
[`pyperclip`](https://pypi.org/project/pyperclip/) -
[`screeninfo`](https://pypi.org/project/screeninfo/)  

from 0.2.6 onwards  
[`pygame`](https://pypi.org/project/pygame/) -
[`PyOpenGL`](https://pypi.org/project/PyOpenGL/) -
[`numpy`](https://pypi.org/project/numpy/) -
[`pillow`](https://pypi.org/project/Pillow/) -
[`opencv-python`](https://pypi.org/project/opencv-python/) -
[`pyperclip`](https://pypi.org/project/pyperclip/) -
[`screeninfo`](https://pypi.org/project/screeninfo/)

## Example of use
```py
import sys
import MGE

MGE.Program.init()

gif = MGE.Object2D([0, 0], 0, [500, 500])
gif.set_material(MGE.Material(MGE.Texture(MGE.Image("./image.gif"))))

MGE.Program.screen.set_size(500, 500)
MGE.Program.set_clock(120)

while True:
    if MGE.Program.get_events()["quit"] or MGE.keyboard("f1"):
        sys.exit()
        
    MGE.Program.screen.clear_screen()
    
    gif.draw_object(MGE.Program.screen)

    MGE.Program.set_caption(f"Gif-MGE | FPS:{int(MGE.Program.get_fps())}")
    MGE.Program.update()
```

- ### Another examples
  [Open Gif](https://github.com/lucas224112/MGE_Open_Gif) - 
  [Text Box](https://github.com/lucas224112/MGE_Text_Box)
