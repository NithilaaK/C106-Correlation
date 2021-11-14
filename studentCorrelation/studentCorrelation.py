import plotly.express as px
import csv
import numpy as np
 
def getDataSource(data_path):
    marks = []
    present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            present.append(float(row['Days Present']))
    return {"x":marks, "y":present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in % vs. Days Present: ", correlation[0, 1])

def plotMarks():
    with open("studentCorrelation/marks.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def setup():
    data_path = "studentCorrelation/marks.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plo = input("Would you like to plot this information (Y/N)? ")
    if (plo == "Y"):
        plotMarks()
    elif (plo == "N"):
        print("OK.")

setup()