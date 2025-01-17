import sys
import time
import cv2
from confluent_kafka import Producer
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
}

topic = "distributed-video1"

def delivery_report(err, msg):
    if err is not None:
        logger.error(f'Message delivery failed: {err}')
    else:
        logger.debug(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def publish_video(video_file):
    """
    Publish given video file to a specified Kafka topic. 
    """
    try:
        producer = Producer(conf)
        video = cv2.VideoCapture(video_file)
        
        logger.info('Publishing video...')

        while video.isOpened():
            success, frame = video.read()
            if not success:
                logger.warning("Bad read!")
                break
            
            # Convert image to jpg
            ret, buffer = cv2.imencode('.jpg', frame)
            
            # Produce message
            producer.produce(
                topic, 
                buffer.tobytes(),
                callback=delivery_report
            )
            producer.poll(0)
            
            time.sleep(0.2)
            
    except Exception as e:
        logger.error(f"Error in publish_video: {e}")
    finally:
        video.release()
        producer.flush()
        logger.info('Publish complete')

def publish_camera():
    """
    Publish camera video stream to specified Kafka topic.
    """
    try:
        producer = Producer(conf)
        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            raise Exception("Could not open camera")
        
        logger.info("Camera opened successfully")
        
        while True:
            success, frame = camera.read()
            if not success:
                logger.warning("Failed to read camera")
                break
                
            ret, buffer = cv2.imencode('.jpg', frame)
            
            producer.produce(
                topic, 
                buffer.tobytes(),
                callback=delivery_report
            )
            producer.poll(0)
            
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        logger.info("\nStopping the stream...")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
    finally:
        if 'camera' in locals():
            camera.release()
        if 'producer' in locals():
            producer.flush()
        logger.info("Resources released")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
        publish_video(video_path)
    else:
        print("publishing feed!")
        publish_camera()