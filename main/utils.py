import matplotlib.pyplot as plt
import base64
from io import BytesIO
import math

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot_bar(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (6,5))
    #plt.title('Daily expenses')
    
    plt.bar(x,y)
    if len(x)!=0:
        new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
        plt.xticks(new_list)
    plt.xlabel('Day')
    plt.ylabel('EXP Amount')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_pie(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize = (6,5))
    #plt.title('Category wise expense')
    plt.pie(y,labels=x,autopct='%0.1f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph