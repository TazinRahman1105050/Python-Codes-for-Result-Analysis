#Python library import
import statistics

#Read input files
input_file = open("Input.fasta", 'r')
Lines = input_file.readlines()

#Define COunter variables
counter = 0
length = []

#Main body of the code to read the input reads
for line in Lines:

    line = line.strip()
    if line[0] != ">":

        counter += int(len(line))

        length.append(int(len(line)))


''' Print Statistics '''
print("Input total lenght in base-paris")
print(counter)

print("Avg input lenght")
print(float(counter)/len(length))

print("Total input reads")
print(len(length))

print("Min input read length")
print(min(length))

print("Max input read length")
print(max(length))

print("Standard Deviation of input reads")
print(statistics.pstdev(lenght))