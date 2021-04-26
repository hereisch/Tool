# -*- coding: utf-8 -*-#
import json
import os
import time
import tkinter
import tkinter.messagebox
import cv2
from PIL import Image, ImageTk





if __name__ == '__main__':

    name = input('请输入文件夹：')
    folder = './samples_0420'
    d = name.strip()
    with open(os.path.join(folder, d, 'pos.json'), ) as f:
        data = json.loads(f.read())
        new = {}
        for item in data['samples']:
            # print(item['id'],item['x'],item['y'])
            new[os.path.split(item['path'])[-1]] = {"x": item['x'], "y": item['y']}
    print(new)
    for i in os.listdir(os.path.join(folder, d)):
        if i.endswith('jpg'):
            imgHW = Image.open(os.path.join(folder, d, i))
            width = imgHW.size[0]
            high = imgHW.size[1]
            img = cv2.imread(os.path.join(folder, d, i))

            x = new[i]['x']
            y = new[i]['y']

            print(d, '/', i, '\t', (x, y))
            cv2.circle(img, (int(x / 1920 * width), int(y / 1080 * high)), 15, (0, 0, 255), -1)
            cv2.putText(img, d + '/' + i, (10, 30), 1, 1.5, (255, 0, 255), 2)
            cv2.putText(img, str((x, y)), (int(x/ 1920 * width - 20), int(y / 1080 * high - 20)), 1, 1.5, (255, 0, 255), 2)
            cv2.imshow('im', img)
            cv2.waitKey(0)