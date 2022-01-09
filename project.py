import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)   #35.05
population_stddev=statistics.stdev(data)  #5.69

print("Mean of population :- ",population_mean)
print("std_deviation of population:- ",population_stddev)

#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

#code to find mean and std deviation of 100 data points

dataset = []
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)    
std_dev=statistics.stdev(dataset)

print("Mean of population :- ",mean)   #35.41
print("std_deviation of population:- ",std_dev) #5.386

# We shall make 1000 groups . In each group there will be 100 samples.

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()


#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()


#Standard deviation of sampling mean
#distribution = Standard Deviation of Population / sqrt (number of data in each sample)
