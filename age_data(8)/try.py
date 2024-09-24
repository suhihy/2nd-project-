import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager


# CSV 파일 불러오기
df = pd.read_csv('thusday.csv')

# 한글 폰트 설정 (Windows에서 Malgun Gothic 폰트를 사용)
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 연령대별 시청자 수 관련 열 선택
age_columns = ['10대(시청자수)', '20대(시청자수)', '30대(시청자수)', '40대(시청자수)', '50대(시청자수)']

# 채널별로 연령대 시청자 수 평균 구하기
channel_age_avg = df.groupby('채널')[age_columns].mean().reset_index()

# 데이터 확인
print(channel_age_avg)

# melt를 사용하여 데이터를 연령대별로 변환
melted_df = channel_age_avg.melt(id_vars='채널', var_name='연령대', value_name='시청자수')

# 시각화 설정
plt.figure(figsize=(12, 6))
sns.lineplot(x='연령대', y='시청자수', hue='채널', data=melted_df, marker='o')

# y축 범위 설정
plt.ylim(0, 500000)

# 그래프 레이블 설정
plt.title('채널별 연령대 시청자 수 분포')
plt.xlabel('연령대')
plt.ylabel('평균 시청자수')
plt.xticks(rotation=45)

# 그래프 표시
plt.tight_layout()
plt.show()

