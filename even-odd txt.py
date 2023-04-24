# PABUNA, KATRINA B.
# Pseudocode
# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt.
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

def process():
    # Open numbers.txt (read), even.txt (append), odd.txt (append)
    with open("numbers.txt") as input_numbers, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:
        # Read integers line by line
        for line in input_numbers:
            input_numbers = int(line)

# ===== start =====
process()