import pyautogui
import time
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)
    return

def Collision(data):
    # cactus
    # for i in range(298, 324):
    #     for j in range(563, 690):
    #         if data[i,j] > 111:
    #             hit('up')
    #             return
    # for i in range(300, 415):
    #     for j in range(410, 563):
    #         if data[i, j] > 111:
    #             hit("down")
    #             return
    # return
    for i in range(450, 500):
        for j in range(500, 558):
            if data[i, j] > 85:
                hit("down")
                return
    for i in range(450, 500):

        for j in range(559, 650):
            if data[i, j] > 85:
                hit("space")
                return
    return
if __name__ == '__main__':
    print("Starting game in 4secs...")
    time.sleep(4)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        Collision(data)
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(370, 400):
    #     for j in range(500, 558):
    #         data[i,j] = 100
    # for i in range(370, 400):
    #     for j in range(559, 650):
    #         data[i,j] = 0
    # image.show()