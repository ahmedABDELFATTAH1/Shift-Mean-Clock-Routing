 
from sklearn.cluster import MeanShift
import numpy as np
import matplotlib.pyplot as plt

colorCount = 0
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
    
def PlotFun(lists, labels = None, Origin = None):
    print(lists)
    print("========================")
    global colorCount 
    x = lists[:,0:1]
    y = lists[:,1:2]
    plt.plot(x,y,'o',color=Colors[colorCount])


    if(labels is not None):
        count = 0
        for i in labels:
            x = [lists[i][0], Origin[count][0]]
            y = [lists[i][1], Origin[count][1]]
            plt.plot(x, y, color = Colors[colorCount])
            count = count + 1

    
    colorCount = colorCount+1
    if(colorCount == len(Colors)):
        colorCount = 0

if _name_ == "_main_":
    ArrOfArr = []
    Input = np.array([[3, 5], [2, 3]  ,[-5, -5],[-5, -3]  ,[-3, 5], [-2, 3],  [5, -5], [5, -3],[2, 2], [2, -2],[-2, 2], [-2, -2]])
    Colors = ["green", "red", "blue", "black", "yellow", "orange"]
    
    PlotFun(Input)

    # exit()

    Cluster(2,Input)
    plt.show()
