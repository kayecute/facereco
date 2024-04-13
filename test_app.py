# filename: test_app.py
import os
import pytest
from unittest import mock
import tkinter as tk
import app  # Sửa tên module nếu cần

# Mock os.system để không thực sự chạy các lệnh shell trong test cases
@mock.patch('os.system', mock.MagicMock())
def test_get_faces_from_camera_tkinter():
    app.get_faces_from_camera_tkinter()
    os.system.assert_called_with('python get_faces_from_camera_tkinter.py')

# Lặp lại tương tự cho mỗi hàm mà bạn muốn test
@mock.patch('os.system', mock.MagicMock())
def test_features_extraction_to_csv():
    app.features_extraction_to_csv()
    os.system.assert_called_with('python features_extraction_to_csv.py')

@mock.patch('os.system', mock.MagicMock())
def test_face_reco_from_camera():
    app.face_reco_from_camera()
    os.system.assert_called_with('python face_reco_from_camera.py')

@mock.patch('os.system', mock.MagicMock())
def test_face_reco_from_camera_single_face():
    app.face_reco_from_camera_single_face()
    os.system.assert_called_with('python face_reco_from_camera_single_face.py')

@mock.patch('os.system', mock.MagicMock())
def test_face_reco_from_camera_ot():
    app.face_reco_from_camera_ot()
    os.system.assert_called_with('python face_reco_from_camera_ot.py')

# Mock messagebox để trả về True khi nó được gọi, như vậy có thể test phần thoát chương trình
@mock.patch('tkinter.messagebox.askokcancel', return_value=True)
def test_on_closing(exit_mock):
    app.on_closing()
    exit_mock.assert_called_once_with("Exit", "Do you want to exit?")
