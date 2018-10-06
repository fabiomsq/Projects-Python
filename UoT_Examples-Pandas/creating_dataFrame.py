import pandas as pd
df = pd.DataFrame (
               data=[
                     [8, 128, 27.5],
                     [10, 138.9, 34.5],
                     [16, 157.3, 91.1],
                     [6, 116.6, 21.4],
                     [14, 159.2, 54.4]
               ],
               columns=['Age', 'Height', 'Weight']
     )
print (df)
