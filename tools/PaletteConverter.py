
def color_to_8bit(val):
    switcher = {
        0: 0,
        1: 36,
        2: 72,
        3: 108,
        4: 144,
        5: 180,
        6: 216,
        7: 255
    }
    return switcher.get(val, 999)


green_mask = 0x01C0
red_mask   = 0x0038
blue_mask  = 0x0007
newFileBytes = []
newFileByteArray = bytes(newFileBytes)
with open('MM1Extra.pal', 'wb') as newFile:
    with open("MM1Extra.dump", "rb") as f:
        while (bword := f.read(2)):
            swap_data = int.from_bytes(bword, byteorder='little', signed=False)
            green_3bit = (green_mask & swap_data) >> 6
            red_3bit   = (red_mask & swap_data) >> 3
            blue_3bit  = (blue_mask & swap_data)
            
            red_8bit   = color_to_8bit(red_3bit)
            green_8bit = color_to_8bit(green_3bit)
            blue_8bit  = color_to_8bit(blue_3bit)
           # print(red_8bit, green_8bit, blue_8bit)
            newFileByteArray += red_8bit.to_bytes(length=1, byteorder='big')
            newFileByteArray += green_8bit.to_bytes(length=1, byteorder='big')
            newFileByteArray += blue_8bit.to_bytes(length=1, byteorder='big')
    # print (newFileByteArray)
    newFile.write(newFileByteArray)
    newFile.close