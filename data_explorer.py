import pandas as pd
import matplotlib.pyplot as plt

mj_data = pd.read_csv('mj-life_mini.csv')
mj_stroke = mj_data[mj_data.psick11 == 1]
# visit count
visit_count = mj_data.groupby(['nn'])['pid'].nunique()
visit_count_s = mj_stroke.groupby(['nn'])['pid'].nunique()
# vc_all_s = pd.merge(visit_count, visit_count_s, how='outer', on=['nn'])
# vc_all_s.rename(columns={'pid_x':'All', 'pid_y':'Stroke'}, inplace=True)
# vc_all_s.fillna(0, inplace=True)
# ax = vc_all_s.plot(kind='bar', secondary_y='Stroke')
# ax.set_xlabel('Visit count')
# ax.set_ylabel('Subject number')
# plt.show()

# first-ever stroke
first__stroke_time = mj_stroke.groupby(['pid'], as_index=False)['n'].min()
first__stroke = pd.merge(mj_data, first__stroke_time, on=['pid', 'n'])
vistit_before_stroke = first__stroke.groupby(['n'])['pid'].nunique()
ax = vistit_before_stroke.plot(kind='bar')
ax.set_xlabel('Visit count')
ax.set_ylabel('Subject number')
plt.show()
print('done')


