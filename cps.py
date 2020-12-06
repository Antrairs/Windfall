'''
python cps.py image_name size(xxx,xxx) [-o new_image_name]
'''

from sys import argv
from re import match
from PIL import Image

if __name__ == '__main__':
    im_path = argv[1]
    m = match('([0-9]+),([0-9]+)', argv[2])
    x1 = int(m.group(1))
    y1 = int(m.group(2))
    im = Image.open(im_path)
    x2, y2 = im.size
    if x1>x2 or y1>y2:
        raise ValueError("需求大小必须小于图片大小")
    if (a := x1 / x2) > (b := y1 / y2):
        y_ = y1 / a
        x_ = x2
        half = (y2 - y_) / 2
        im = im.crop((0, half, x2, y2 - half))
    else:
        x_ = x1 / b
        y_ = y2
        half = (x2 - x_) / 2
        im = im.crop((half, 0, x2 - half, y2))

    im = im.resize((x1, y1))
    if len(argv) > 3 and argv[3] == '-o':
        im.save(argv[4])

    else:
        im.save(f'_{argv[1]}')
