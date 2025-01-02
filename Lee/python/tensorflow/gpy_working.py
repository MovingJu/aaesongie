import tensorflow as tf

# TensorFlow와 GPU를 사용할 준비가 되었는지 확인
print("TensorFlow Version:", tf.__version__)
print("GPU is", "available" if tf.config.list_physical_devices('GPU') else "NOT AVAILABLE")

# GPU 정보를 출력
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        print(f"GPU Name: {gpu}")
else:
    print("No GPU detected.")
