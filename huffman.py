import numpy as np
import heapq

# Class representing a node in the Huffman tree
class HuffmanNode:
    def __init__(self, symbol, probability):
        self.symbol = symbol  # The symbol (grayscale value)
        self.probability = probability  # The probability of the symbol
        self.left = None  # Left child
        self.right = None  # Right child

    # Comparison operator for priority queue (heap)
    def __lt__(self, other):
        return self.probability < other.probability

# Function to build the Huffman tree from symbol probabilities
def build_huffman_tree(probabilities):
    try:
        # Create a heap (priority queue) of Huffman nodes
        heap = [HuffmanNode(symbol, prob) for symbol, prob in probabilities.items()]
        heapq.heapify(heap)
        
        # Merge nodes until only one node remains (the root of the Huffman tree)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)  # Remove the node with the smallest probability
            node2 = heapq.heappop(heap)  # Remove the next smallest node
            merged = HuffmanNode(None, node1.probability + node2.probability)  # Create a new internal node
            merged.left = node1  # Set the left child
            merged.right = node2  # Set the right child
            heapq.heappush(heap, merged)  # Add the new node back to the heap
        
        return heap[0]  # Return the root of the Huffman tree
    except Exception as e:
        raise RuntimeError(f"Failed to build Huffman tree: {e}")

# Function to generate Huffman codes from the Huffman tree
def generate_huffman_codes(node, prefix="", codebook={}):
    try:
        if node is not None:
            if node.symbol is not None:
                codebook[node.symbol] = prefix  # Assign the code to the symbol
            generate_huffman_codes(node.left, prefix + "0", codebook)  # Traverse left with '0'
            generate_huffman_codes(node.right, prefix + "1", codebook)  # Traverse right with '1'
        return codebook
    except Exception as e:
        raise RuntimeError(f"Failed to generate Huffman codes: {e}")

# Function to display Huffman codes sorted by symbol
def display_huffman_codes(huffman_codes):
    try:
        for symbol in sorted(huffman_codes.keys()):
            print(f"Symbol: {symbol}, Code: {huffman_codes[symbol]}")
    except Exception as e:
        raise RuntimeError(f"Failed to display Huffman codes: {e}")

# Function to compute the average length of the Huffman codes
def compute_average_code_length(probabilities, huffman_codes):
    try:
        avg_length = sum(probabilities[symbol] * len(code) for symbol, code in huffman_codes.items())
        return avg_length
    except Exception as e:
        raise RuntimeError(f"Failed to compute average code length: {e}")

# Function to compute the compression ratio
def compute_compression_ratio(original_bits, avg_code_length):
    try:
        return original_bits / avg_code_length
    except Exception as e:
        raise RuntimeError(f"Failed to compute compression ratio: {e}")

# Function to compute the Shannon entropy of the symbol probabilities
def compute_shannon_entropy(probabilities):
    try:
        entropy = -sum(prob * np.log2(prob) for prob in probabilities.values())
        return entropy
    except Exception as e:
        raise RuntimeError(f"Failed to compute Shannon entropy: {e}")