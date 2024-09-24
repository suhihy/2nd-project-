import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# CSV 파일 읽기
df = pd.read_csv('~/Desktop/DMF/youtube_data/youtube_api/금쪽상담소_comment_df.csv', header=None, names=['video_id', 'comment_time'])

# 'comment_time'을 datetime 형태로 변환, 변환 불가한 값은 NaT로 처리
df['comment_time'] = pd.to_datetime(df['comment_time'], errors='coerce')

# NaT 값을 제외한 나머지 데이터로 분석 진행
df = df.dropna(subset=['comment_time'])

# 'comment_time'을 30분 단위로 그룹화
df['Time_Bin'] = df['comment_time'].dt.floor('30T').dt.time

# 시간대별 댓글 수 계산
time_counts = df.groupby('Time_Bin').size().reset_index(name='comment_count')

# 시간대 정렬
time_counts = time_counts.sort_values('Time_Bin')

# 바 그래프 그리기
plt.figure(figsize=(12, 8))
bars = plt.bar(time_counts['Time_Bin'].astype(str), time_counts['comment_count'], color='b')

# 각 막대 위에 댓글 수 레이블 추가 (댓글 수가 10개 이상인 경우에만)
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    if height >= 10:
        plt.text(x, height, str(int(height)), ha='center', va='bottom', fontsize=9)

# 그래프 제목과 축 레이블 설정
plt.title('Number of Comments per 30-Minute Interval')
plt.xlabel('Time (30-minute intervals)')
plt.ylabel('Number of Comments')

# x축 레이블 설정 (시간)
plt.xticks(rotation=45, ha='right')

# 그래프 출력
plt.tight_layout()
plt.show()
