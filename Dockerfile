# Sử dụng một base image có sẵn
FROM ubuntu:20.04

# Thiết lập thông tin tác giả
LABEL maintainer="drneetotaku@gmail.com>"

# Cài đặt các dependencies và ứng dụng cần thiết
RUN apt-get update && apt-get install -y \
    nginx \
    python \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập môi trường làm việc
WORKDIR /app

# Sao chép mã nguồn ứng dụng vào container
COPY . .

# Mở cổng mặc định cho ứng dụng (nếu cần)
EXPOSE 80

# Chạy ứng dụng khi container được khởi chạy
CMD ["python", "app.py"]
