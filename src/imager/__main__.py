from .imager import Imager
from .builder import build_code
import cv2

import eel
import bottle

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from os.path import dirname

path = dirname(__file__)

app = bottle.default_app()

imager = Imager(path + "/mona-lisa.jpg", name="mona-lisa")

eel.init(path + "/assets")

@eel.expose
def update_file(): # borrowed from https://github.com/brentvollebregt/auto-py-to-exe/blob/master/auto_py_to_exe/dialogs.py
    """ Ask the user to select a file """
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    filetypes = [("Image PNG", "*.png"), ("Image JPG", ".jpg"), ("All files", "*")]
    filepath = askopenfilename(parent=root, filetypes=filetypes)
    root.update()

    # bool(filepath) will help filter our the negative cases; an empty string or an empty tuple
    if bool(filepath):
        global imager

        imager = Imager(filepath, name=filepath)

        return filepath

@eel.expose
def update_scale(value):
    imager.pixelate(float(value))

    return value


@eel.expose
def generate_code():
    return build_code(imager)

@bottle.get("/image")
def generate_preview():
    preview = imager.preview()

    _, buffer = cv2.imencode(".png", preview)

    return buffer.tobytes()

def main():
    eel.start("index.html", app=app)

if __name__ == "__main__":
    main()