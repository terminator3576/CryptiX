import hashlib
import secrets

class SecureRNG:
    def __init__(self, seed=None):
        # Convert the seed to bytes if it's an integer
        self.seed = seed.to_bytes(32, byteorder='big') if isinstance(seed, int) else (seed or secrets.token_bytes(32))  
        self.counter = 0  # Counter to ensure different outputs for each call

    def next_int(self, min_value=1, max_value=1000000, num_bytes=4):
        """
        Generate a cryptographically secure pseudorandom integer.
        """
        self.counter += 1
        hash_input = self.seed + self.counter.to_bytes(16, byteorder='big')
        
        # Use SHA-256 to generate hash and get desired length by slicing
        hash_output = hashlib.sha256(hash_input).digest()[:num_bytes]

        random_value = int.from_bytes(hash_output, byteorder='big')
        return min_value + (random_value % (max_value - min_value + 1))

    def next_bytes(self, num_bytes=4):
        """
        Generate cryptographically secure random bytes of a specified length.
        """
        self.counter += 1 
        hash_input = self.seed + self.counter.to_bytes(16, byteorder='big')
        return hashlib.sha256(hash_input).digest()[:num_bytes]

def main_random(min_value, max_value, seed):
  x = SecureRNG(seed) 
  return x.next_int(min_value, max_value)
