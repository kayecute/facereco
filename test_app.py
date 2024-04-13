import pytest
from unittest.mock import patch
import app

def test_on_closing():
    with patch('tkinter.messagebox.askokcancel', return_value=True):
        app.on_closing()

def test_run_script():
    script_name = "test_script.py"
    with patch('os.system') as mock_system:
        app.run_script(script_name)
        mock_system.assert_called_once_with(f"python {script_name}")

# Bổ sung thêm các testcase cho các hàm khác trong app.py nếu cần

if __name__ == '__main__':
    pytest.main()
