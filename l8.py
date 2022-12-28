import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.widgets import Slider, Button
import re

def sel_sort(array, ax):
        i = 0

        for i in range(len(array)):
                m = i
                j = i + 1
                while j < len(array):
                    if array[j] < array[m]:
                        m = j
                    j = j + 1
                array[i], array[m] = array[m], array[i]
                ax.cla()
                for i in range(len(array)):           
                    ax.scatter(i, array[i])
                plt.pause(1)
    
        

def main():  

    fig, ax = plt.subplots()

    plt.subplots_adjust(left=0.25, bottom=0.3)

    a = [int(el) for el in input().split()]
  
    for i in range(len(a)):           
        ax.scatter(i, a[i])



    def f1(event):        
        sel_sort(a, ax)
        
        


    axbutton_orange1 = plt.axes([0.07, 0.8, 0.1, 0.075])
    borange1 = Button(axbutton_orange1, 'start')
    borange1.on_clicked(f1)

    
    plt.show()
    

    

if __name__ == "__main__":
    main()
