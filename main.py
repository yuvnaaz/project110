import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data copy.csv")
un_data = df["responses"].tolist()
data = []

for i in un_data:
    if i.isnumeric():
        data.append(int(i))

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

sample_data = []

def getSample(counter):
    ds = []
    for i in range(0 ,counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        ds.append(value)
    mean = statistics.mean(ds)
    return mean

def setup():
    for i in range(0, 100):       
        sample_data.append(getSample(30))
    plot_graph(sample_data)

def plot_graph(data):
    fig = ff.create_distplot([data], ["Claps"], show_hist = False)
    fig.show()
setup()

sample_mean = statistics.mean(sample_data)

print(f"The Mean of the data is : {mean:.3f}")
print(f"The Mean of the sample is : {sample_mean:.3f}")