# Image Processing

import io
import cvlib as cv
import numpy as np
from cvlib.object_detection import draw_bbox
from PIL import Image

# load corrupted images (may cause errors)
#Image.LOAD_TRUNCATED_IMAGES = True

def detect_objects(input_img, debug = False):
    try:
        # convert recieved bytes to image
        img = np.array(np.array(Image.open(io.BytesIO(input_img))))
        width = img.shape[1]
        height = img.shape[0]
        bbox, label, conf = cv.detect_common_objects(img)
        if debug:
            # draw bounding box on image and save to disk
            output_image = draw_bbox(img, bbox, label, conf)
            Image.fromarray(output_image).save("output_" + input_img)
        if bbox == []:
            return "", []
        bbox_w = bbox[0][0] + (bbox[0][2] - bbox[0][0]) / 2
        bbox_h = bbox[0][1] + (bbox[0][3] - bbox[0][1]) / 2
        obj_coord = [width, height, bbox_w, bbox_h]
        return label[0], obj_coord
    except:
        return "", []

def convert_coord(obj_coord):
    # find location of object in image and convert to coordinates on OLED
    width, height, obj_w, obj_h = obj_coord
    display_coord_w = int(obj_w / width * 128)
    display_coord_h = int((obj_h - (height - width / 2) / 2) / height * 64)
    if display_coord_h < 0:
        display_coord_h = 0
    if display_coord_h < 0:
        display_coord_h = 63
    if display_coord_w > 128:
        display_coord_w = 128
    return [display_coord_w, display_coord_h]


if __name__ == '__main__':
    # test with local image
    label, obj_coord = detect_objects("test.jpeg", True)
    display = convert_coord(obj_coord)
    print(label)
    print(obj_coord)
    print(display)