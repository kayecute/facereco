import tkinter as tk
import tkinter.messagebox as messagebox
import os

def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

def auto_exit():
    if messagebox.askokcancel("Auto Exit", "The app will now exit after running for 5 minutes."):
        root.destroy()


root = tk.Tk()
root.title('GUI for Face Recognition')
root.geometry('1300x550')

window_width = 1300
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def run_script(script_name):
    os.system(f"python {script_name}")

def get_faces_from_camera_tkinter():
    os.system('python get_faces_from_camera_tkinter.py')

def features_extraction_to_csv():
    os.system('python features_extraction_to_csv.py')

def face_reco_from_camera():
    os.system('python face_reco_from_camera.py')

def face_reco_from_camera_single_face():
    os.system('python face_reco_from_camera_single_face.py')

def face_reco_from_camera_ot():
    os.system('python face_reco_from_camera_ot.py')

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

button_frame = tk.Frame(main_frame)
button_frame.pack(side='top', fill='x', padx=10)

get_faces_button = tk.Button(button_frame, text='Get Faces from Camera', command=get_faces_from_camera_tkinter)
get_faces_button.pack(side='left', padx=10)

features_extraction_button = tk.Button(button_frame, text='Features Extraction to CSV', command=features_extraction_to_csv)
features_extraction_button.pack(side='left', padx=10)

face_reco_button = tk.Button(button_frame, text='Face Recognition from Camera (Multi Face)', command=face_reco_from_camera)
face_reco_button.pack(side='left', padx=10)

face_reco_single_button = tk.Button(button_frame, text='Face Recognition from Camera (Single Face)', command=face_reco_from_camera_single_face)
face_reco_single_button.pack(side='left', padx=10)

face_reco_single_button = tk.Button(button_frame, text='Better Face Recognition from Camera (Single Face)', command=face_reco_from_camera_ot)
face_reco_single_button.pack(side='left', padx=10)

root.after(300000, root.destroy())

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
