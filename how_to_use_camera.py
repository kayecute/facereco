import cv2

cap = cv2.VideoCapture(0)

# cap.set(propId, value)
# Set video parameters: propId - set video parameters, value - set parameter value
"""
0. cv2.CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. cv2.CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
2. cv2.CAP_PROP_POS_AVI_RATIO Relative position of the video file
3. cv2.CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4. cv2.CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5. cv2.CAP_PROP_FPS Frame rate.
6. cv2.CAP_PROP_FOURCC 4-character code of codec.
7. cv2.CAP_PROP_FRAME_COUNT Number of frames in the video file.
8. cv2.CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9. cv2.CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10. cv2.CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11. cv2.CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12. cv2.CAP_PROP_SATURATION Saturation of the image (only for cameras).
13. cv2.CAP_PROP_HUE Hue of the image (only for cameras).
14. cv2.CAP_PROP_GAIN Gain of the image (only for cameras).
15. cv2.CAP_PROP_EXPOSURE Exposure (only for cameras).
16. cv2.CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
17. cv2.CAP_PROP_WHITE_BALANCE Currently unsupported
18. cv2.CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
"""

# The default size of frame from camera will be 640x480 in Windows or Ubuntu
# So we will not set "cap.set" here, it doesn't work
# cap.set(propId=cv2.CAP_PROP_FRAME_WIDTH, value=cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# cap.isOpened()  true/false,
print(cap.isOpened())

# cap.read()

while cap.isOpened():
    ret_flag, img_camera = cap.read()

    print("height: ", img_camera.shape[0])
    print("width:  ", img_camera.shape[1])
    print('\n')

    cv2.imshow("camera", img_camera)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite("test.jpg", img_camera)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
