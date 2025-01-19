# Video Streaming with Kafka

Dự án này thực hiện streaming video (từ webcam hoặc video file) sử dụng Apache Kafka và Flask.

## Yêu cầu hệ thống

- Python 3.8+
- Docker và Docker Compose
- Webcam (nếu muốn stream từ camera)

## Cài đặt

1. **Clone repository:**
   ```bash
   git clone https://github.com/vuminhhieuu/big-data-beginer.git
   cd big-data-beginer/videostreaming
   ```

2. **Tạo và kích hoạt môi trường ảo:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Cài đặt các dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Khởi động Kafka và Zookeeper:**
   ```bash
   docker-compose up -d
   ```

## Chạy ứng dụng

1. **Khởi động consumer (Flask server):**
   ```bash
   python consumer.py
   ```
   Server sẽ chạy tại http://localhost:5000

2. **Khởi động producer:**

   - Để stream từ webcam:
     ```bash
     python producer.py
     ```

   - Để stream từ file video:
     ```bash
     python producer.py path/to/video.mp4
     ```

## Xử lý sự cố

### Lỗi webcam
Nếu gặp lỗi khi truy cập webcam:
1. Kiểm tra webcam có được kết nối đúng cách
2. Đảm bảo không có ứng dụng khác đang sử dụng webcam
3. Kiểm tra quyền truy cập webcam
4. Thử sử dụng video file thay thế

### Lỗi Kafka
Nếu không kết nối được với Kafka:
1. Kiểm tra containers có đang chạy:
   ```bash
   docker ps
   ```
2. Kiểm tra logs:
   ```bash
   docker-compose logs
   ```

## Dừng ứng dụng

1. Dừng producer và consumer bằng `Ctrl+C`

2. Dừng Kafka và Zookeeper:
   ```bash
   docker-compose down
   ```

## Công nghệ sử dụng

- **Apache Kafka**: Message broker
- **Flask**: Web framework
- **OpenCV**: Xử lý video
- **Docker**: Container platform

## Lưu ý

- Đảm bảo ports 2181 (Zookeeper), 9092 (Kafka), và 5000 (Flask) không bị sử dụng bởi ứng dụng khác
- Điều chỉnh độ phân giải và frame rate trong `producer.py` nếu cần thiết
- Có thể điều chỉnh giao diện web trong `templates/index.html`

## Đóng góp

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo issue hoặc pull request.

## License

[MIT License](LICENSE)