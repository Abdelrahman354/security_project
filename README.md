# security_project
This code is a Python script that creates a graphical user interface (GUI) using the Tkinter library to implement several encryption algorithms. The implemented algorithms are Caesar Cipher, Vigenere Cipher, Playfair Cipher, and DES Encryption.

The GUI has several input fields for the plaintext, key, and buttons to initiate encryption/decryption. The results are displayed in labels on the GUI. The different encryption algorithms are implemented as functions in the code.

The Caesar Cipher implementation takes a plaintext and a key, which is an integer representing the number of positions to shift each character in the plaintext. The plaintext is converted to uppercase, and each character is shifted by the key value using the alphabet array.

The Vigenere Cipher implementation takes a plaintext and a key, which is a string representing the keyword to be used for encryption. The plaintext and key are converted to uppercase, and a matrix is created using the alphabet array. The corresponding row and column values for each character in the plaintext and key are used to look up the encrypted character in the matrix.

The Playfair Cipher implementation takes a plaintext and a key, which is a string representing the keyword to be used for encryption. The plaintext is converted to uppercase, and any double letters are separated by a filler character (in this implementation, 'X'). A matrix is created using the keyword, and the corresponding row and column values for each character in the plaintext are used to look up the encrypted character in the matrix.

The DES Encryption implementation takes a plaintext anda key, which is a string representing the secret key used for encryption. The plaintext is encrypted using the pyDes library, which implements the Data Encryption Standard (DES) algorithm. The resulting ciphertext is displayed in hexadecimal format.

Overall, this code provides a simple graphical interface for implementing different encryption algorithms, making it easy for users to test and understand the workings of these algorithms.
