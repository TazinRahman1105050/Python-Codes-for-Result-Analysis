#import required libraries
import matplotlib.pyplot as plt
import numpy as np

#Read input files
Input_log_file = open("Ipput.log", 'r')
Lines = Input_log_file.readlines()


#Define the arrays for x and y axis
x = []
RepeatedKmers = []
NonGenomicKmers = []
UniqueKmers = []

#We are runiing the for loop for 50 times since we are interest in frequency upto 50
for i in range (1,51):
    x.append(i)
    RepeatedKmers.append(0)
    NonGenomicKmers.append(0)
    UniqueKmers.append(0)
print(x)


#Read the input
for line in Lines:
    line= line.strip()
    lt = line.split(' ')
    if int(lt[2]) == 0:

        if int(lt[1]) in x:
            NonGenomicKmers[int(lt[1]) -1] += 1
    elif int(lt[2]) == 2:

        if int(lt[1]) in x:
            UniqueKmers[int(lt[1]) -1] += 1
    else:
        if int(lt[1]) in x:
            RepeatedKmers[int(lt[1]) - 1] += 1





#Create the plots

y1 = np.array(NonGenomicKmers)
y2 = np.array(UniqueKmers)
y3 = np.array(RepeatedKmers)
plt.yscale("log") # Use log scale
# plot bars in stack manner
plt.bar(x, y2, color='g') # Green bar for Unique Kmers
plt.bar(x, y3, bottom=y2, color='r') # Red bar for Repeated Kmers
plt.bar(x, y1, bottom=y2 + y3, color='b') # Blue bar for Non-Genomic Kmers

plt.xlabel("k-mer frequency", fontsize=20)
plt.ylabel("#k-mers for a frequency", fontsize=20)
plt.legend([ "unique k-mer", "repeated k-mer", "non-genomic k-mer"], fontsize=20)
plt.title("k-mer frequency distribution", fontsize=20)
plt.yticks(fontsize= 20)
plt.xticks(fontsize=20)
plt.show()