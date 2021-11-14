import plotly.express as px
import csv
import numpy as np
 
def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {"x":coffee, "y":sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml vs. Sleep in hours: ", correlation[0, 1])

def plotCoffee():
    with open("coffeeCorrelation/coffee.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def setup():
    data_path = "coffeeCorrelation/coffee.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plo = input("Would you like to plot this information (Y/N)? ")
    if (plo == "Y"):
        plotCoffee()
    elif (plo == "N"):
        print("OK.")

setup()