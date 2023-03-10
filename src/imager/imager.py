import cv2
import numpy as np

from base64 import b85encode
from gzip import compress

from .const import table
from .const import ENCODING

class Imager:
    def __init__(self, filepath, name="untitled") -> None:
        self.bitmap = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        
        
        self.name = name

        self.height, self.width = self.bitmap.shape
        self.pixelate(1)
    
    def translate(self):
        instructions = "["
        
        for row in self.pixelated_bitmap:
            instructions += "[" + ",".join(map(str, row)) + "],"
        
        instructions += "]"

        compiled = b85encode(compress(instructions.encode(ENCODING))).decode(ENCODING)

        return compiled
    
    def pixelate(self, scale):
        self.height, self.width = int(self.bitmap.shape[0] * scale), int(self.bitmap.shape[1] * scale)
        
        # pixelate bitmap
        self.pixelated_bitmap = cv2.resize(self.bitmap, (self.width, self.height), interpolation=cv2.INTER_LINEAR)

        # normalize values to indexes in table
        self.pixelated_bitmap //= round(256 / len(table))

        return self.pixelated_bitmap
    
    def preview(self):
        changed_colors = list(map(lambda row: list(map(lambda item: table[item], row)), self.pixelated_bitmap))

        preview = np.array(changed_colors, dtype=np.uint8)
        preview = cv2.resize(preview, (self.bitmap.shape[1], self.bitmap.shape[0]), 0, 0, interpolation=cv2.INTER_NEAREST)
        preview = cv2.cvtColor(preview, cv2.COLOR_RGB2BGR)
        
        return preview