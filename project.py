import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_population = statistics.mean(data)
stdev_population = statistics.stdev(data)
print(mean_population)
print(stdev_population)
#fig = ff.create_distplot([data],["average"],show_hist=False)
#fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["Reading Time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.3],mode="lines",name="Mean"))
    fig.show()
    
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean_sample=statistics.mean(mean_list)
    stdev_sample=statistics.stdev(mean_list)
    print("mean of sample distribution", mean_sample)
    print("standard of sample distribution", stdev_sample)
setup()