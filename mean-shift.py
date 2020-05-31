from sklearn.cluster import MeanShift
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog,Text
import os

def Cluster(BW, arr):
    if(len(arr) == 1):
        return 0

    clustering = MeanShift(bandwidth=BW).fit(arr)
    if(len(clustering.cluster_centers_) == len(arr)):
        Cluster(BW+1,arr)
    else:
        PlotFun(clustering.cluster_centers_,clustering.labels_,arr)
        ArrOfArr.append(clustering.cluster_centers_)
        Cluster(BW,clustering.cluster_centers_)
    
def PlotFun(lists, labels = None, Origin = None, pointColor="blue"):
    print(lists)
    print("========================")
    if len(lists) == 1:
        pointColor = "red" 
    x = lists[:,0:1]
    y = lists[:,1:2]
    plt.plot(x,y,'o',color=pointColor)


    if(labels is not None):
        count = 0
        for i in labels:
            x = [lists[i][0], Origin[count][0]]
            y = [lists[i][1], Origin[count][1]]
            plt.plot(x, y, color = "black")
            count = count + 1


    # plt.show()


def getorigin(eventorigin):    
      print("orign")
      x = eventorigin.x
      y = eventorigin.y
      print(x,700-y)      
      canavas.create_oval(x, y, x, y, width = 10, fill = 'blue')    
      Input.append([x,700-y])
      

def savePoints():
    print("save")   
    Cluster(2,Input)    
    PlotFun(np.array(Input),pointColor = "green")
    plt.show()
    canavas.delete('all') 
    Input.clear()
    

if __name__=="__main__":
    ArrOfArr = []
    Input = []
    Colors = ["green", "red", "blue", "black", "yellow", "orange" , "Aqua", "Medium Gray", "Navy Blue"]   
    root = tk.Tk()    
    pointsbutton=tk.Button(root,text="run wiring",padx=10,pady=5,fg="blue",command=savePoints)  
    T = tk.Text(root, height=2, width=100)
    T.pack()
    T.insert(tk.END, "Welcome , draw some sink clock points then press run wiring button ")
    T1 = tk.Text(root, height=2, width=300)
    T1.pack()
    T1.insert(tk.END, "This simulation is made by Sofyan , Ahmed Abdelfattah ,Ahmed Nassar And Mokhtar .")    
    canavas=tk.Canvas(root,height=700,width=700,bg="#FFFFFF")
    canavas.bind("<Button 1>",getorigin)
    pointsbutton.pack()
    canavas.pack()   
    root.mainloop()