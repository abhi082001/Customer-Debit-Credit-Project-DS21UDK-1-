import matplotlib.pyplot as plt

import base64
from io import BytesIO
import math
import pandas as pd

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot_bar1(x,y,xt,yt):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    #x.sort()
    x = [str(i) for i in x]
    y=list(y)
    l=[]
    for i in range(len(x)):
        l.append([x[i],y[i]])
    l.sort()
    x=[i[0] for i in l]
    y=[i[1] for i in l]
    data = pd.DataFrame(y, columns=['values'])
    plt.barh(x,y,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    
    
    '''
    if len(x)!=0:
        new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
        plt.yticks(new_list)
    '''
    
    
    for index, value in enumerate(y):
        plt.text(value, index, str(value))
    
    
    plt.ylabel(yt)
    plt.xlabel(xt)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_bar(x,y,xt,yt):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    
    l = []
    M= ['January','February','March','April','May','June','July','August','September','October','November','December']
    for m in M:
        if m in x:
            l.append([m,y[x.index(m)]])
    
    x = [i[0] for i in l]
    y_1=[i[1] for i in l]
    data = pd.DataFrame(y_1, columns=['values'])
    plt.barh(x,y_1,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    
    for index, value in enumerate(y_1):
        plt.text(value, index, str(value))
    
    plt.ylabel(yt)
    plt.xlabel(xt)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_pie(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (6,5))
    l=[]
    for i in range(len(x)):
        if y[i]!=0:
            l.append([x[i],y[i]])
    x=[i[0] for i in l]
    y=[i[1] for i in l]
    plt.pie(y,labels=x,autopct='%0.1f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_line1(x,y,xt,yt):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    
    l = []
    M= ['January','February','March','April','May','June','July','August','September','October','November','December']
    for m in M:
        if m in x:
            l.append([m,y[x.index(m)]])
    x = [i[0] for i in l]
    y_1=[i[1] for i in l]
    data = pd.DataFrame(y_1, columns=['values'])
    #plt.barh(x,y_1,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    plt.scatter(x,y_1)
    plt.plot(x,y_1)
    
    plt.xticks(rotation=30)
    plt.ylabel(xt)
    plt.xlabel(yt)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_line(x,y,xt,yt):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    
    x = [str(i) for i in x]
    y=list(y)
    l=[]
    for i in range(len(x)):
        l.append([x[i],y[i]])
    l.sort()
    x=[i[0] for i in l]
    y=[i[1] for i in l]
    #plt.barh(x,y_1,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    plt.scatter(x,y)
    plt.plot(x,y)
    '''
    for index, value in enumerate(y):
        plt.text(value, index, str(value))
    '''
    #plt.xticks(rotation=45)
    plt.ylabel(xt)
    plt.xlabel(yt)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_count(x,y,xt,yt):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    #x.sort()
    x = [str(i) for i in x]
    y=list(y)
    l=[]
    for i in range(len(x)):
        l.append([x[i],y[i]])
    l.sort()
    x=[i[0] for i in l]
    y=[i[1] for i in l]
    plt.bar(x,y)
    plt.scatter(x,y)
    plt.ylabel(yt)
    plt.xlabel(xt)
    plt.tight_layout()
    graph = get_graph()
    return graph