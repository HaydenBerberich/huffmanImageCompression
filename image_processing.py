import cv2
from collections import Counter

def load_image(image_path):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        return image
    except Exception as e:
        raise RuntimeError(f"Failed to load image: {e}")

def compute_histogram(image):
    try:
        histogram = Counter(image.flatten())
        return histogram
    except Exception as e:
        raise RuntimeError(f"Failed to compute histogram: {e}")

def compute_probabilities(histogram, total_pixels):
    try:
        probabilities = {k: v / total_pixels for k, v in histogram.items()}
        return probabilities
    except Exception as e:
        raise RuntimeError(f"Failed to compute probabilities: {e}")