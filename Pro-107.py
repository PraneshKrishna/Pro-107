import pandas as pd
import plotly.express as px
import csv
import plotly.graph_objects as go



df = pd.read_csv("PixelMath.csv")

print(df.groupby("level")["attempt"].mean())

mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
fig = px.scatter(mean,x = "student_id",y = "level", size = "attempt", color = "attempt")
fig.show()
