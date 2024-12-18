# Hayden Berberich
# 12-2-2024

from image_processing import load_image, compute_histogram, compute_probabilities
from huffman import build_huffman_tree, generate_huffman_codes, compute_average_code_length, compute_compression_ratio, display_huffman_codes, compute_shannon_entropy
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Huffman Coding Compression')
parser.add_argument('image_path', type=str, help='Path to the grayscale image')
args = parser.parse_args()

# Path to the grayscale image
image_path = args.image_path

try:
    # Load the grayscale image
    image = load_image(image_path)

    # Compute the histogram and probabilities of the grayscale values
    histogram = compute_histogram(image)
    total_pixels = image.size
    probabilities = compute_probabilities(histogram, total_pixels)

    # Build the Huffman tree and generate Huffman codes
    huffman_tree = build_huffman_tree(probabilities)
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Compute the average code length and compression ratio
    avg_code_length = compute_average_code_length(probabilities, huffman_codes)
    original_bits = 8  # Each pixel in a grayscale image is 8 bits
    compression_ratio = compute_compression_ratio(original_bits, avg_code_length)

    # Display the Huffman codes and compute Shannon entropy
    display_huffman_codes(huffman_codes)
    shannon_entropy = compute_shannon_entropy(probabilities)

    # Print the results
    print(f"Average code length: {avg_code_length}")
    print(f"Compression ratio: {compression_ratio}")
    print(f"Shannon entropy: {shannon_entropy}")

except Exception as e:
    print(f"An error occurred: {e}")