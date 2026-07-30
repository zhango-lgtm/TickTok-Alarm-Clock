import pandas as pd

DATABASE = "sqlite:///ticktok.db"

columns = ["run_id", "user_name", "alarm_react", "g1", "g2", "g3", "g4", "g5", "total_time"]
df_empty = pd.DataFrame(columns=columns)
df_empty.to_sql("runs", con=DATABASE, if_exists="replace", index=False)

print("Database ticktok.db created successfully!")
