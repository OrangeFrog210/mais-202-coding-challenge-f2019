import pandas as pd
import matplotlib.pyplot as plt

# please change the file path as appropriate.
fIN1 = r"C:\Users\Yumika\Downloads\mais-202-coding-challenge-f2019-master\mais-202-coding-challenge-f2019-master\loan_data.csv"
fIN2 = r"C:\Users\Yumika\Downloads\mais-202-coding-challenge-f2019-master\mais-202-coding-challenge-f2019-master\home_ownership_data.csv"

df1, df2 = pd.read_csv(fIN1), pd.read_csv(fIN2)

# merging the two data frames based on member_id
df3 = df1.merge(df2, left_on="member_id", right_on="member_id")
# determining the average loan amount for each of the home ownership status
df4 = df3.groupby('home_ownership', as_index=False)['loan_amnt'].mean()
print(df4)

ax = df4.plot.bar(x="home_ownership", rot=0, title="Average loan amounts per home ownership")
ax.set_xlabel("Home ownership", fontsize=12)
ax.set_ylabel("Average loan amount ($)", fontsize=12)
plt.show()
