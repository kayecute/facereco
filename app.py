import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess

def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

def run_script(script_name):
    try:
        subprocess.run(f"python {script_name}", check=True, shell=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Execution Error", f"An error occurred while running {script_name}.n{e}")

def get_faces_from_camera_tkinter():
    run_script('get_faces_from_camera_tkinter.py')

def features_extraction_to_csv():
    run_script('features_extraction_to_csv.py')

def face_reco_from_camera():
    run_script('face_reco_from_camera.py')

def face_reco_from_camera_single_face():
    run_script('face_reco_from_camera_single_face.py')

def face_reco_from_camera_ot():
    run_script('face_reco_from_camera_ot.py')

root = tk.Tk()
root.title('GUI for Face Recognition')
root.geometry('1300x550')

button_frame = tk.Frame(root)
button_frame.pack(pady=20, padx=20)

get_faces_button = tk.Button(
    button_frame,
    text='Get Faces from Camera',
    command=get_faces_from_camera_tkinter
)
get_faces_button.pack(side='left', padx=10)

features_extraction_button = tk.Button(
    button_frame,
    text='Features Extraction to CSV',
    command=features_extraction_to_csv
)
features_extraction_button.pack(side='left', padx=10)

face_reco_button = tk.Button(
    button_frame,
    text='Face Recognition from Camera (Multi Face)',
    command=face_reco_from_camera
)
face_reco_button.pack(side='left', padx=10)

face_reco_single_button = tk.Button(
    button_frame,
    text='Face Recognition from Camera (Single Face)',
    command=face_reco_from_camera_single_face
)
face_reco_single_button.pack(side='left', padx=10)

face_reco_ot_button = tk.Button(
    button_frame,
    text='Better Face Recognition from Camera (Single Face)',
    command=face_reco_from_camera_ot
)
face_reco_ot_button.pack(side='left', padx=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
