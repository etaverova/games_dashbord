import pandas as pd

visits_df = pd.read_csv('data/dash_visits.csv')

visits_df['date'] = visits_df['date'].apply(lambda x: str(x)[:10])