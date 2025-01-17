from flask import Flask, Response, render_template
from confluent_kafka import Consumer
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'video-group',
    'auto.offset.reset': 'latest'
}

try:
    consumer = Consumer(conf)
    consumer.subscribe(['distributed-video1'])
    logger.info("Kafka Consumer connected successfully")
except Exception as e:
    logger.error(f"Error connecting to Kafka: {e}")
    consumer = None

# Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(
        get_video_stream(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logger.error(f"Consumer error: {msg.error()}")
                continue
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpg\r\n\r\n' + msg.value() + b'\r\n\r\n')
    except Exception as e:
        logger.error(f"Error in video stream: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)