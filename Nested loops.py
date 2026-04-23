# =========================================
# File: nested_loops_bio_examples.py
# Author: Kalyan
# Description:
# Practice of nested loops with biological examples
# =========================================

import time


# ==============================
# 1. BASIC NESTED LOOP COUNT
# ==============================

list1 = list(range(1, 10))
list2 = list(range(1, 10))

count = 0

for i in list1:
    count += 1
    for j in list2:
        count += 1

print("Total iterations:", count)


# ==============================
# 2. PATTERN PRINTING
# ==============================

for i in range(5):
    for j in range(5):
        print("0", end="")
    print()


# ==============================
# 3. PERFORMANCE (NO PRINT)
# ==============================

start = time.time()

for i in range(100):
    for j in range(100):
        pass

end = time.time()

print("Execution time:", round(end - start, 4), "seconds")


# ==============================
# 4. MATRIX TRAVERSAL
# ==============================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ==============================
# 5. DNA SEQUENCE SIMILARITY
# ==============================

dna1 = "ATGCTAGCTAG"
dna2 = "ATGCTAGATAG"

similarity = 0

for i in range(len(dna1)):
    if dna1[i] == dna2[i]:
        similarity += 1

print("Similarity count:", similarity)


# ==============================
# 6. FIND MATCHING BASES
# ==============================

for base1 in dna1:
    for base2 in dna2:
        if base1 == base2:
            print("Matching base:", base1)


# ==============================
# 7. CODON GENERATION
# ==============================

rna = "AUGCGAUAGCGAUAGCU"

for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if len(codon) == 3:
        print("Codon:", codon)


# ==============================
# 8. DOT PLOT (SEQUENCE COMPARISON)
# ==============================

seq1 = "ATGC"
seq2 = "ATGC"

for i in seq1:
    for j in seq2:
        print("*" if i == j else ".", end=" ")
    print()


# ==============================
# 9. REVERSE COMPLEMENT
# ==============================

dna = "ATGCTAGC"

complement_map = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_complement = "".join(complement_map[b] for b in dna)[::-1]

print("Reverse Complement:", reverse_complement)


# ==============================
# 10. LOOP CHALLENGE (ENUMERATE)
# ==============================

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62]

count = 0

for index, value in enumerate(num_list):
    print(value)

    print("Over 45" if value > 45 else "Under 45")

    count += 1

    if value == 36:
        print(f"Number found at position: {index}")
        break

print("Total processed:", count)


# ==============================
# 11. LOOP EXERCISE (ENUMERATE + BREAK)
# ==============================

"""
Exercise Objective:
- Practice loops, conditions, enumerate, and break
- Track count and stop when a condition is met
"""

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0

for index, value in enumerate(num_list):

    print("Value:", value)

    print("Over 45" if value > 45 else "Under 45")

    count += 1

    if value == 36:
        print(f"Number found at position: {index}")
        break

print(f"Total numbers processed before break: {count}")