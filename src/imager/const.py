table = [ # block and its RGB values
    [7, 9, 14], # 'black concrete'
    [57, 42, 35], # 'gray terracotta'
    [77, 50, 36], # 'brown terracotta'
    [135, 106, 97], # 'light gray terracotta'
    [207, 175, 160], # 'white terracotta'
    [227, 224, 202], # 'bone block'
    [238, 230, 222], # 'smooth quartz block'
    [247, 254, 254], # 'snow'
]

blocks = [ # /setblock ~ ~ ~ <block name> <id>
    "concrete 15", # black concrete
    "stained_hardened_clay 7", # grey terracotta
    "stained_hardened_clay 12", # brown terracotta
    "stained_hardened_clay 8", # light grey terracotta
    "stained_hardened_clay 0", # light terracotta
    "bone_block 0", # bone block
    "quartz_block 3", # smooth quartz
    "snow 0", # snow block
]

# offset agent
OFFSET_X = 0
OFFSET_Y = 0
OFFSET_Z = 0

ENCODING = "utf-8" # used encoding for instructions

SPEED_PER_BLOCK = 0.1 # average speed per block in seconds

def time2human(secs):
    secs = round(secs)

    days = secs // 86400
    hours = secs // 3600 % 24
    minutes = secs // 60 % 60
    seconds = secs % 60

    return (days, hours, minutes, seconds)