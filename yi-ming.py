import pandas as pd

mj_data = pd.read_csv('relate21a.csv')
# mj_data = pd.read_csv('min.csv')
mj_data_at_least_3 = (mj_data.groupby(['pid']).size() > 2).reset_index(name='at_least_3')
mj_data_at_least_3_id = mj_data_at_least_3[mj_data_at_least_3.at_least_3].pid
mj_data_at_least_3_df = mj_data[mj_data.pid.isin(mj_data_at_least_3_id)]
first_report_time = mj_data_at_least_3_df.groupby(['pid'], as_index=False)['n'].min()

df_result = None
for i, r in first_report_time.iterrows():
    pid = r['pid']
    n = r['n']
    df_1 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n)].reset_index()
    df_2 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n+1)].reset_index()
    df_3 = mj_data_at_least_3_df[(mj_data_at_least_3_df.pid == pid) & (mj_data_at_least_3_df.n == n+2)].reset_index()
    if(~(df_2.empty | df_3.empty)):
        df_2 = df_2.add_suffix('_2')
        df_3 = df_3.add_suffix('_3')
        if df_result is None:
            df_result = pd.concat([df_1, df_2, df_3], axis=1)
        else:
            df_temp = pd.concat([df_1, df_2, df_3], axis=1)
            df_result = pd.concat([df_result, df_temp])
    # print(pid)
df_result.drop(['index'], inplace=True, axis=1)
df_result.to_csv('relate21a_3times.csv', index=False)
# print('done')