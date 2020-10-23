import matplotlib.pyplot as plt
import sys
import pandas as pd

number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.003,0.082,0.333,1.328,5.332,12.023,21.335,33.394,133.253,299.158,532.317,831.562]
plt.subplots(1,1,figsize=(10,4),sharey=True ,dpi =120)
plt.title("Merge Sort vs Heap Sort vs Bubble Sort vs Insertion Sort vs Quick Sort")
plt.ylabel("Time")
plt.xlabel("Number")

plt.plot(number,tm,"-",label='BubbleSort')

number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.0,0.001,0.003,0.008,0.028,0.064,0.113,0.178,0.723,1.652,2.95,4.571]
#plt.subplots(1,1,figsize=(10,4),sharey=True ,dpi =120)
#plt.title("QuickSort")
#plt.ylabel("Time")
#plt.xlabel("Number")

plt.plot(number,tm,'-',label='QuickSort')
#plt.savefig("quicksort.png")
#plt.show()

number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.0,0.013,0.051,0.206,0.825,1.87,3.308,5.178,20.783,46.897,84.333,131.204]
#plt.subplots(1,1,figsize=(10,4),sharey=True ,dpi =120)
#plt.title("Insertion Sort")
#plt.ylabel("Time")
#plt.xlabel("Number")

plt.plot(number,tm,'-',label='InsertionSort')

number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.0,0.001,0.001,0.002,0.004,0.006,0.009,0.011,0.022,0.035,0.047,0.059]
#plt.subplots(1,1,figsize=(10,4),sharey=True ,dpi =120)
#plt.title("MergeSort")
#plt.ylabel("Time")
#plt.xlabel("Number")

plt.plot(number,tm,'-',label='MergeSort')

number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.0,0.0,0.001,0.001,0.001,0.001,0.001,0.001,0.003,0.004,0.005,0.005]
#plt.plot(number,tm,'-',label='MergeSort Thread')


number=[1000,5000,10000,20000,40000,60000,80000,100000,200000,300000,400000,500000]
tm=[0.0,0.0,0.002,0.004,0.007,0.01,0.014,0.017,0.036,0.054,0.073,0.094]
#plt.subplots(1,1,figsize=(10,4),sharey=True ,dpi =120)
#plt.title("HeapSort")
#plt.ylabel("Time")
#plt.xlabel("Number")
plt.plot(number,tm,'-',label='HeapSort')

plt.savefig("sorts.png")
plt.legend()
plt.show()