import pandas as pd 
import plotly.figure_factory as ff

df = pd.read_csv("mobile brand vs avg rating.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()
