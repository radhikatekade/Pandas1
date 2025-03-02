import pandas as pd

# Two-dimensional list
data = [['English', '82'],
        ['Math', '96'],
        ['Science', '75']]

df = pd.DataFrame(data, columns = ["Subject", "Marks"])
print(df)