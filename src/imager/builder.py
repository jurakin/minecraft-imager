from .const import SPEED_PER_BLOCK

from .const import OFFSET_X
from .const import OFFSET_Y
from .const import OFFSET_Z

from .const import ENCODING

from .const import blocks

from .const import time2human

def _format_total_time(used_blocks):
        return "{}d {}h {}m {}s".format(*time2human(used_blocks * SPEED_PER_BLOCK))

def build_code(imager):
    instructions = imager.translate()
    name = imager.name
    width = imager.width
    height = imager.height

    if any((instructions, name, width, height)) is None: raise ValueError("instructions, name, width, height must be defined")

    used_blocks = width * height
    total_time = _format_total_time(used_blocks)
    
    # write configurations and instructions
    code = f"""
#  __  __ _                            __ _     ___                                 
# |  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_  |_ _|_ __ ___   __ _  __ _  ___ _ __ 
# | |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __|  | || '_ ` _ \ / _` |/ _` |/ _ \ '__|
# | |  | | | | | |  __/ (__| | | (_| |  _| |_   | || | | | | | (_| | (_| |  __/ |   
# |_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__| |___|_| |_| |_|\__,_|\__, |\___|_|   
#                                                                   |___/           

# ========== CONFIGURATIONS ========== #
NAME = "{name}"

OFFSET_X = {OFFSET_X}
OFFSET_Y = {OFFSET_Y}
OFFSET_Z = {OFFSET_Z}

WIDTH = {width}
HEIGHT = {height}

USED_BLOCKS = {used_blocks}

TOTAL_TIME = "{total_time}"

BLOCKS = {blocks}
# ======== END CONFIGURATIONS ======== #

# =========== INSTRUCTIONS =========== #
from base64 import b85decode
from gzip import decompress
instructions = eval(decompress(b85decode("{instructions}")).decode("{ENCODING}"))
# ========= END INSTRUCTIONS ========= #
"""

    # write the main code
    code += """
import time

# print function
def print(*text): agent.say(*text)

def command(*cmd):
    with agent._command("execute", "@c", "~ ~ ~", *cmd) as data:
        return data

def setblock(x, y, z, block): command(f"setblock ~{x} ~{y} ~{z} {block}")

# Print basic info about printing
print("=" * 10)
print(f"Image : {NAME}")
print(f"Size  : {WIDTH}x{HEIGHT}")
print(f"Total : {USED_BLOCKS}")
print( "Time  : {TOTAL_TIME}")
print("=" * 10)

time.sleep(10)

print("Imager is running ...")

d1 = time.time()

for y, row in enumerate(bitmap):
    for x, block in enumerate(row):
        block_coors = OFFSET_X + x, OFFSET_Y + y, OFFSET_Z

        setblock(*block_coors, blocks[block])
    
    percent = round(y / HEIGHT * 100)
    
    print(f"Printing: {percent}%")

d2 = time.time()

print("Imager ended!")
print(f"Elapsed: {d2-d1}s")
show_title("The End", f"Elapsed: {d2-d1}s")
"""
    return code