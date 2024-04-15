# test_app.py
import os
from unittest import mock
import pytest
import tkinter as tk
import app  # Giả sử tất cả các hàm được test đều trong file này

# Ghi chú: Bạn cần đảm bảo rằng app.py chứa các hàm được test.
# Ví dụ:
# def get_faces_from_camera_tkinter():
#     os.system('python get_faces_from_camera_tkinter.py')
# ...

# Sử dụng mock.patch như decorator để thay thế os.system trong môi trường test
@mock.patch('os.system')
def test_get_faces_from_camera_tkinter(mocked_system):
    app.get_faces_from_camera_tkinter()
    mocked_system.assert_called_with('python get_faces_from_camera_tkinter.py')

@mock.patch('os.system')
def test_features_extraction_to_csv(mocked_system):
    app.features_extraction_to_csv()
    mocked_system.assert_called_with('python features_extraction_to_csv.py')

@mock.patch('os.system')
def test_face_reco_from_camera(mocked_system):
    app.face_reco_from_camera()
    mocked_system.assert_called_with('python face_reco_from_camera.py')

@mock.patch('os.system')
def test_face_reco_from_camera_single_face(mocked_system):
    app.face_reco_from_camera_single_face()
    mocked_system.assert_called_with('python face_reco_from_camera_single_face.py')

@mock.patch('os.system')
def test_face_reco_from_camera_ot(mocked_system):
    app.face_reco_from_camera_ot()
    mocked_system.assert_called_with('python face_reco_from_camera_ot.py')

# Đối với việc test hàm on_closing, bạn cần mock tkinter.messagebox.askokcancel
# và cũng cần chắc chắn rằng 'root' được handle đúng cách trong app.py
@mock.patch('tkinter.messagebox.askokcancel', return_value=True)
@mock.patch('app.root', create=True)  # Mock 'root' nếu cần thiết
def test_on_closing(mocked_askokcancel, mocked_root):
    app.on_closing()
    mocked_askokcancel.assert_called_once_with("Exit", "Do you want to exit?")
    # Kiểm tra xem các method của 'root' đã được gọi chưa, ví dụ:
    assert mocked_root.quit.called
    assert mocked_root.destroy.called

# Chạy tất cả tests với pytest
if __name__ == "__main__":
    pytest.main()
