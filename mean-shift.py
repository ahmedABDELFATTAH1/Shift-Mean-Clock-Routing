from sklearn.cluster import MeanShift
import numpy as np
import matplotlib.pyplot as plt

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

if _name_ == "_main_":
    ArrOfArr = []
    Input = np.array([[3, 5], [2, 3]  ,[-5, -5],[-5, -3]  ,[-3, 5], [-2, 3],  [1, -5], [3, -3],[2, 2],[-2, 2]])
    Colors = ["green", "red", "blue", "black", "yellow", "orange" , "Aqua", "Medium Gray", "Navy Blue"]
    

    # exit()

    Cluster(2,Input)
    PlotFun(Input,pointColor = "green")
    plt.show()
