import tkinter as tk
import tkinter.messagebox as messagebox
import os
import face_descriptor_from_camera,face_reco_from_camera,face_reco_from_camera_single_face,face_reco_from_camera_ot,get_faces_from_camera,get_faces_from_camera_tkinter,features_extraction_to_csv,features_extraction_to_csv
root = None
# Định nghĩa hàm gọi khi thoát ứng dụng
def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        try:
            root.quit()
            root.destroy()
        except tk.TclError as e:
            print("Window already closed:", e)
def auto_exit():
    if messagebox.askokcancel("Auto Exit", "The app will now exit after running for 5 minutes."):
        try:
            root.quit()
            root.destroy()
        except tk.TclError as e:
            print("Window already closed:", e)
def main():
    global root
    root = tk.Tk()
    root.title('GUI for Face Recognition')
    root.geometry('1300x550')
    # Đặt cửa sổ tại vị trí giữa màn hình
    window_width = 1300
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # Cấu hình sự kiện thoát
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Tạo và định cấu hình các phần tử giao diện tại đây
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
    # Đây chỉ là một số nút ví dụ. Định cấu hình hành động của bạn tại đây.
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    get_faces_button = tk.Button(button_frame, text='Get Faces from Camera', command=lambda: run_script('get_faces_from_camera_tkinter.py'))
    get_faces_button.pack(side='left', padx=10)
    # Thêm nút và hành động khác tương tự ở đây nếu cần
    # Chương trình sẽ tự đóng sau 5 phút
    root.after(300000, auto_exit)
    root.mainloop()
# Hàm này được dùng để chạy một script Python từ giao diện Tkinter. Nó dùng os.system(), một cách đơn giản nhưng không phải là lựa chọn tốt nhất vì nó không cho biết kết quả của lệnh và có thể gây ra các vấn đề bảo mật.
# Cân nhắc lựa chọn khác như subprocess.run() cho sản phẩm thực tế.
def run_script(script_name):
    os.system(f"python {script_name}")
if __name__ == '__main__': # Đảm bảo rằng đây là __name__ không phải name
    main()