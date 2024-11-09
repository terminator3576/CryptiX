# 🔒 CryptiX
### Python-based Hashing Software

**CryptiX** is a customizable hashing algorithm built in Python. With adjustable security levels, it allows you to control the balance between processing time and hash security.

---

## 🚀 How to Use CryptiX

1. **Prepare Input**  
   - Place your input text in `input.txt`.

2. **Set Security Level**  
   - Choose a security level; higher values will shuffle bits more thoroughly, increasing randomness and security at the cost of longer processing time.

3. **Run the Algorithm**  
   - The algorithm shuffles bits, pads/shortens the output, and uses a Merkle–Hellman cryptosystem variation for a strong hash.

4. **View Output**  
   - The final hash output appears after processing based on your chosen security level.

---

## ⏱️ Processing Times

Below are sample timings based on different security levels and input sizes:

| **Security Level** | **1 Character**   | **10 Characters** | **100 Characters** |
|--------------------|-------------------|-------------------|--------------------|
| **100**           | < 1 second       | < 1 second       | < 1 second        |
| **1,000**         | < 1 second       | < 1 second       | 1 second          |
| **10,000**        | < 1 second       | < 1 second       | 3 seconds         |
| **100,000**       | 1 second         | 4 seconds        | 27 seconds        |
| **1,000,000**     | 10 seconds       | 20 seconds       | 3 minutes         |

> ⏳ **Note**: Higher security levels increase processing time, especially with large inputs.

---

## 🌟 Planned Enhancements

To improve performance and hash reliability, the following updates are planned:

1. **Block Processing**  
   - Split input into 512- or 1024-bit blocks, reducing processing time without sacrificing security.

2. **Parallel Processing**  
   - Divide input into chunks for parallel shuffling and hashing, ideal for large inputs.

3. **Enhanced Mixing Step**  
   - Apply XOR with prime-based rotations or matrix transformations to ensure greater bit diffusion.

4. **Merkle-Damgård Construction**  
   - Use a construction where each input block’s hash builds on the previous one (as in MD5 and SHA-1) for improved reliability.

5. **Nonlinear Hash Functions**  
   - Introduce operations like modular exponentiation with a prime modulus to increase hash sensitivity to input changes.
  
---

## 📋 Known Limitations

- **Large Message Processing**: Very large messages can take longer to hash.
- **Small Changes Sensitivity**: Minor input changes may not always alter the final hash.
- **Inefficient Shortening Function**: The shortening step could be optimized for better performance.
- **Time-Intensive Operations**: The Fisher-Yates shuffle consumes the most processing time.

> 💡 **Suggestions?** Feel free to contribute ideas or optimizations!
