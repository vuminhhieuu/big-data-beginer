# Big Data Beginer Projects with Apache Kafka

Tập hợp các bài tập thực hành về xử lý dữ liệu với Apache Kafka, tập trung vào các ứng dụng streaming data trong thời gian thực.

## Giới thiệu về Apache Kafka

[Apache Kafka](https://kafka.apache.org/) là một nền tảng streaming phân tán mã nguồn mở, được thiết kế để xử lý luồng dữ liệu theo thời gian thực. Kafka được sử dụng rộng rãi cho:
- Stream Processing
- Real-time Analytics
- Log Aggregation
- Event Sourcing
- Message Queuing

### Các khái niệm cơ bản
- **Producer**: Ứng dụng gửi messages vào Kafka
- **Consumer**: Ứng dụng đọc và xử lý messages từ Kafka
- **Topic**: Danh mục để tổ chức và lưu trữ messages
- **Broker**: Server Kafka, quản lý việc lưu trữ và truyền messages
- **Partition**: Phân vùng của topic, cho phép xử lý song song

## Danh sách Projects

### 1. CSV Streaming
Ứng dụng demo về stream dữ liệu từ file CSV sử dụng Kafka và Python.
- [Chi tiết và hướng dẫn](./csvstreaming/README.md)
- Dựa trên hướng dẫn từ [Towards Data Science](https://towardsdatascience.com/make-a-mock-real-time-stream-of-data-with-python-and-kafka-7e5e23123582)

### 2. Video Streaming
Ứng dụng streaming video realtime với Kafka và Flask.
- [Chi tiết và hướng dẫn](./videostreaming/README.md)
- Dựa trên hướng dẫn từ [Medium](https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd)


### 3. Anomaly Detection
Ứng dụng phát hiện bất thường trong thời gian thực với Kafka và Machine Learning.
- [Chi tiết và hướng dẫn](./anomalydetection/README.md)
- Dựa trên hướng dẫn từ [Towards Data Science](https://towardsdatascience.com/real-time-anomaly-detection-with-apache-kafka-and-python-3a40281c01c9)

## Yêu cầu hệ thống

### Môi trường phát triển
- Python 
- Docker và Docker Compose
- Git

### Python Dependencies chung
- confluent-kafka>=2.3.0
- flask>=3.0.0
- python-dotenv>=1.0.0


### Yêu cầu Docker
- Docker Engine
- Docker Compose version 2.0+
- Ports cần thiết:
  - 2181: Zookeeper
  - 9092: Kafka
  - 5000: Flask (cho video streaming)

## Cài đặt và Khởi động

1. **Clone repository:**
   ```bash
   git clone https://github.com/vuminhhieuu/big-data-beginer.git
   cd big-data-beginer
   ```

2. **Cài đặt môi trường Python:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Khởi động Kafka và Zookeeper:**
   ```bash
   docker-compose up -d
   ```
## Các lệnh Make có sẵn

- `make setup`: Tạo môi trường ảo và cài đặt dependencies
- `make start`: Khởi động các containers Docker
- `make stop`: Dừng các containers
- `make clean`: Dọn dẹp môi trường (xóa containers, venv, cache)
- `make logs`: Xem logs của các containers
- `make kafka-shell`: Truy cập shell của Kafka container
- `make topics`: Liệt kê các topics trong Kafka

## Cấu trúc thư mục
```
big-data-beginer/
    ├── csvstreaming/        # Demo streaming CSV data
    ├── videostreaming/      # Demo video streaming 
    ├── anomalydetection/    # Demo anomaly detection
    ├── docker-compose.yml   # Docker compose chung
    ├── requirements.txt     # Dependencies chung
    └── README.md
```

## Xử lý sự cố chung

### Kafka
- Kiểm tra trạng thái services:
  ```bash
  make logs
  ```
- Truy cập Kafka shell:
  ```bash
  make kafka-shell
  ```
- Xem danh sách topics:
  ```bash
  make topics
  ```

### Làm sạch và khởi động lại
Nếu gặp vấn đề, có thể reset toàn bộ môi trường:
```bash
make clean
make setup
make start
```

