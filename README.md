Caesar Cipher Brute Force – Python
📌 Description

This project demonstrates how the Caesar cipher works and how it can be broken using a brute-force attack.
The Caesar cipher is a classical substitution cipher in which each letter in the plaintext is shifted by a fixed number of positions in the alphabet. Since there are only 25 possible shifts, it is highly vulnerable and can be easily cracked by testing all possible combinations.
This script automatically tries every possible shift and prints all candidate plaintext outputs so the correct message can be identified.

🎯 Objective

The purpose of this project is to:
Understand how classical substitution ciphers work
Learn why weak encryption methods are insecure
Apply brute-force logic in Python
Strengthen basic cryptography fundamentals

🛠 Concepts Used
for loops
String manipulation
ASCII conversion using ord() and chr()
Brute-force attack logic

⚙️ How It Works

The user inserts the ciphertext directly into the script.
The program iterates through all 25 possible shifts.
Each shifted result is printed.
The correct plaintext can be visually identified from the output.

▶️ How to Run
Make sure you have Python 3 installed.
python cifrado_cesar.py
It is recommended to use Visual Studio Code or any Python-compatible IDE for execution.

📚 What I Learned
How encryption algorithms operate
Why classical ciphers are insecure
How brute-force attacks exploit limited keyspaces
How to manipulate characters using ASCII values in Python

🚀 Possible Improvements
Allow user input from terminal instead of editing the script
Add automatic detection of the most probable plaintext
Support uppercase and lowercase separately
Add frequency analysis for smarter cracking
