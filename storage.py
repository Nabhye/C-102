import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0) #start the webcam
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False  
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def Upload_File(img_name):
    access_token = 'QuRT1OV_7skAAAAAAAAAARKSegLECoAIwSAJLS6PrRqCk6J5vbFO_w1b3Cl6clSx'
    file = img_name
    file_from = file
    file_to = "/WHJ" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded successfully")

def main():
    while(True):
        if((time.time() - start_time) >= 12):
            name = take_snapshot()
            Upload_File(name)

main()