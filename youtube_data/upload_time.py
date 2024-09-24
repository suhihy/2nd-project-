import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# CSV 파일 읽기 (header 확인)
df = pd.read_csv('~/Desktop/DMF/youtube_data/youtube_api/금쪽이_data_sorted.csv', header=0, names=['video_id', 'title', 'view_count', 'upload_time'])

# 'upload_time'을 datetime 형태로 변환, 변환 불가한 값은 NaT로 처리
df['upload_time'] = pd.to_datetime(df['upload_time'], errors='coerce')

# NaT 값을 제외한 나머지 데이터로 분석 진행
df = df.dropna(subset=['upload_time'])

# 'upload_time'에서 시간만 추출
df['Time_Bin'] = df['upload_time'].dt.floor('10T').dt.time

# 12:30 ~ 13:40 범위를 설정
start_time = datetime.strptime('12:30', '%H:%M').time()
end_time = datetime.strptime('13:40', '%H:%M').time()

# 해당 시간 범위 내의 데이터 필터링
df_within_range = df[(df['Time_Bin'] >= start_time) & (df['Time_Bin'] <= end_time)]

# 시간 범위 외의 데이터 개수 계산
df_outside_range = df[(df['Time_Bin'] < start_time) | (df['Time_Bin'] > end_time)]
print(f"시간 범위(12:30~13:40) 외에 있는 데이터 개수: {len(df_outside_range)}")

# 각 시간대별 업로드된 영상 수 계산 (범위 내의 데이터만)
time_counts = df_within_range.groupby('Time_Bin').size()

# 12:30 ~ 13:40 범위의 전체 시간대(10분 간격) 생성
time_range = pd.date_range('12:30', '13:40', freq='10T').time

# 범위 내의 누락된 구간을 0으로 채운 Series 생성
full_time_counts = pd.Series(0, index=time_range)
full_time_counts.update(time_counts)

# 선 그래프 그리기
plt.figure(figsize=(10, 6))
ax = full_time_counts.plot(kind='line', marker='o', color='b')

# 그래프 제목과 축 레이블 설정
plt.title('Number of Video Uploads between 12:30 and 13:40 (10-Minute Intervals)')
plt.xlabel('Upload Time (10-minute intervals)')
plt.ylabel('Number of Videos')

# x축 레이블 설정 (10분 간격)
plt.xticks(ticks=time_range, labels=[time.strftime('%H:%M') for time in time_range], rotation=45, ha='right')

# y좌표에 영상 개수를 표시
for time, count in full_time_counts.items():
    ax.text(time, count, str(count), ha='center', va='bottom')

# 그래프 출력
plt.tight_layout()
plt.show()
