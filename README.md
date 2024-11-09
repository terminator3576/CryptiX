# CryptiX
python hashing software


**Known limitations**

a) Really large messages take a long time to process and small changes in the message can sometimes not affect the final hash value

b) Shortening function just not very good

c) Function which takes the most time is the Fisher-Yates shuffle

Feel free to give ideas about how to fix this!

**Future updates**

a) Use Block Processing: Instead of shuffling the entire input, process it in smaller, fixed-size blocks (e.g., 512-bit or 1024-bit). This would reduce the time complexity, making it faster without compromising security.

b) Parallel Processing: For large inputs, divide the input into chunks that can be shuffled and hashed in parallel threads. This could substantially reduce the time required for processing.

c) Add a Mixing or Diffusion Step: After the Fisher-Yates shuffle, apply a diffusion function, such as XOR with prime number-based rotations or matrix transformations. This ensures that each bit in the input can affect many bits in the final hash.

d) Implement a Merkle-Damgård Construction: To improve reliability, use a Merkle-Damgård-style construction, where each input block’s hash depends on the previous block. This technique is used in many strong hash functions like MD5 and SHA-1.

e) Incorporate Nonlinear Hash Functions: Integrate a nonlinear operation after shuffling, such as modular exponentiation with a prime modulus. This could introduce more sensitivity to bit changes.


**Use**

1) Enter an input in input.txt
   
2) Enter a security level, this will shuffle the bits more thouroughly the higher the number, reducing the probablility of collisions and increasing apparent randomness, but is a tradeoff between time and security.
   
3) Now the algorithm calculates the hash by first of all shuffling the bits, then padding/shortening the output. Last of all, it uses a variation of the Merkle–Hellman cryptosystem to produce a strong hash. 

4) Finally, you get your output which, without a computer, would take days to calculate. You however don't care and having entered an excessively large security level are wondering why it took so long :)

Timings for level 100:
 - 
 - 1 character, < 1 second
 - 10 characters, < 1 second
 - 100 characters, < 1 second

Timings for level 1,000:
-
 - 1 character, < 1 second
 - 10 characters, < 1 second
 - 100 characters, 1 second

Timings for level 10,000:
-
 - 1 character, < 1 second
 - 10 characters, < 1 second
 - 100 characters, 3 seconds

Timings for level 100,000:
-
 - 1 character, 1 second
 - 10 characters, 4 seconds
 - 100 characters, 27 seconds

Timings for level 1,000,000:
-
 - 1 character, 10 seconds
 - 10 characters, 20 seconds
 - 100 characters, 3 minutes




