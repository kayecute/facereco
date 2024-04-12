import torch
# Kiểm tra xem CUDA có sẵn không và thiết lập biến 'device'
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121  // sử dụng khi GPU của bạn đủ mạnh, ueu tiên RTX2050 trở lên
# thay đô đường đẫn và phiên bản cuda phù hợp với máy của bạn   
print(torch.cuda.is_available())  # Nếu trả về True, bạn đã cài PyTorch với CUDA thành công.
   
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
print(torch.version.cuda)
print(torch.__version__)
print(torch.cuda.get_device_name(0))

