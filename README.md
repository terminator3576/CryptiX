# CryptiX
python hashing software


**Use**

1) Enter an input in input.txt
   
3) Enter a security level, this will shuffle the bits more thouroughly the higher the number, reducing the probablility of collisions and apparent randomness, but is a tradeoff between time and security.
   
4) Now the algorithm calculates the hash by first of all shuffling the bits, then padding/shortening the output. Last of all, it uses a variation of the Merkle–Hellman cryptosystem to produce a strong hash. 

5) Finally, you get your output which, without a computer, would take days to calculate. You however don't care and having entered an excessively large security level are wondering why it took so long :)

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




