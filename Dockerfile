# Sử dụng một base image
FROM python:3.8.13

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy các file cần thiết vào container
COPY . /app

# Nâng cấp pip và cài đặt các dependencies cần thiết để chạy tkinter app
RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y cmake xvfb x11vnc && \
    pip install -r requirements.txt

# Mở port (ví dụ port 80)
EXPOSE 80

# Set up Xvfb và run tkinter app
CMD Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \
    export DISPLAY=:99 && \
    x11vnc -display :99 -usepw -forever -create & \
    python app.py