import pandas as pd
from functools import reduce
mj_data = pd.read_csv('relate21a.csv')
print(mj_data.shape)
# # mj_data = pd.read_csv('min.csv')
mj_data_at_least_3 = (mj_data.groupby(['pid']).size() > 2).reset_index(name='at_least_3')
mj_data_at_least_3_id = mj_data_at_least_3[mj_data_at_least_3.at_least_3].pid
mj_data_at_least_3_df = mj_data[mj_data.pid.isin(mj_data_at_least_3_id)]

# continuing 3 times, very slow but get more data
# first_report_time = mj_data_at_least_3_df.groupby(['pid'], as_index=False)['n'].min()
# df_result = None
# for i, r in first_report_time.iterrows():
#     pid = r['pid']
#     n = r['n']
#     df_1 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n)].reset_index()
#     df_2 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n+1)].reset_index()
#     df_3 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n+2)].reset_index()
#     if(~(df_2.empty | df_3.empty)):
#         df_2 = df_2.add_suffix('_2')
#         df_3 = df_3.add_suffix('_3')
#         if df_result is None:
#             df_result = pd.concat([df_1, df_2, df_3], axis=1)
#         else:
#             df_temp = pd.concat([df_1, df_2, df_3], axis=1)
#             df_result = pd.concat([df_result, df_temp])
#     # print(pid)
# df_result.drop(['index'], inplace=True, axis=1)
# df_result.to_csv('relate21a_3times.csv', index=False)


# top 3 times, fast but less data
df_1 = mj_data_at_least_3_df[mj_data_at_least_3_df.n == 1]
print(df_1.shape)
df_2 = mj_data_at_least_3_df[mj_data_at_least_3_df.n == 2].add_suffix('_2')
df_2.rename(columns={'pid_2':'pid'}, inplace=True)
print(df_2.shape)
df_3 = mj_data_at_least_3_df[mj_data_at_least_3_df.n == 3].add_suffix('_3')
df_3.rename(columns={'pid_3':'pid'}, inplace=True)
print(df_3.shape)
df_merged = reduce(lambda left,right: pd.merge(left,right, on=['pid'],
                                            how='inner'), [df_1, df_2, df_3])
print(df_merged.shape)
df_merged.to_csv('relate21a_3times.csv', index=False)
print('done')