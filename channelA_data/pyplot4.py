import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

# 한글 폰트 설정 (Windows에서 Malgun Gothic 폰트를 사용)
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# CSV 파일 읽기
df = pd.read_csv('family_2023.csv')

# '프로그램명' 열에서 '오은영의금쪽상담소'가 포함된 행 필터링
filtered_df = df[df['프로그램명'].str.contains('선넘은')]

# 시청률 관련 열을 길게 변형하여 프로그램명과 성별, 연령대 정보를 포함하는 데이터프레임 생성
melted_df = filtered_df.melt(
    id_vars=['프로그램명'],
    value_vars=[
        '4-9세 남자 시청률', '4-9세 여자 시청률',
        '10대 남자 시청률', '10대 여자 시청률',
        '20대 남자 시청률', '20대 여자 시청률',
        '30대 남자 시청률', '30대 여자 시청률',
        '40대 남자 시청률', '40대 여자 시청률',
        '50대 남자 시청률', '50대 여자 시청률',
        '60대 이상 남자 시청률', '60대 여자 시청률'
    ],
    var_name='연령대_성별',
    value_name='시청률'
)

# 연령대/성별에 따른 평균 시청률 계산
average_df = melted_df.groupby('연령대_성별')['시청률'].mean().reset_index()

# 시각화
plt.figure(figsize=(14, 8))
sns.barplot(x='연령대_성별', y='시청률', data=average_df, palette='viridis')

# 그래프 제목과 레이블 설정
plt.title('Average Ratings by Age Group and Gender for "선넘은패밀리"')
plt.xlabel('Age Group / Gender')
plt.ylabel('Average Ratings')
plt.xticks(rotation=90)  # X축 레이블 회전

# 그래프를 파일로 저장
plt.tight_layout()
plt.savefig('average_ratings_plot.png', dpi=300)  # dpi=300은 고해상도 설정

# 그래프 표시
plt.show()
