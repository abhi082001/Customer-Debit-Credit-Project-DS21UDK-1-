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

def get_plot_bar1(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (8,5))
    
    data = pd.DataFrame(y, columns=['values'])
    plt.bar(x,y,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    #plt.scatter(x,y_1)
    #plt.bar(x,y)
    
    if len(x)!=0:
        new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
        plt.xticks(new_list)
    '''
    if len(y)!=0:
        new_list = range(math.floor(min(y)), math.ceil(max(y))+1)
        plt.yticks(new_list)
    '''
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_bar(x,y):
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
    plt.bar(x,y_1,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    #plt.scatter(x,y_1)
    #plt.bar(x,y)
    '''
    if len(y)!=0:
        new_list = range(math.floor(min(y)), math.ceil(max(y))+1)
        plt.yticks(new_list)
    '''
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_pie(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (6,5))
    
    plt.pie(y,labels=x,autopct='%0.1f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_line(x,y):
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
    #plt.bar(x,y_1,color=(data['values'] > 0).map({True: 'c', False: 'r'}))
    plt.scatter(x,y_1)
    plt.plot(x,y_1)
    #plt.bar(x,y)
    '''
    if len(y)!=0:
        new_list = range(math.floor(min(y)), math.ceil(max(y))+1)
        plt.xticks(new_list)
    '''
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.tight_layout()
    graph = get_graph()
    return graph