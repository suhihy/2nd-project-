import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기 (header 확인)
df = pd.read_csv('~/Desktop/DMF/youtube_data/youtube_api/금쪽이_data_sorted.csv', header=0, names=['video_id', 'title', 'view_count', 'upload_time'])

# 'Upload_Time'을 datetime 형태로 변환, 변환 불가한 값은 NaT로 처리
df['upload_time'] = pd.to_datetime(df['upload_time'], errors='coerce')

# datetime 변환이 실패한 행을 확인 (NaT 값 확인)
invalid_dates = df[df['upload_time'].isna()]

# 만약 변환이 실패한 날짜가 있으면 출력
if not invalid_dates.empty:
    print("날짜 형식 변환 실패 행:")
    print(invalid_dates)

# NaT 값을 제외한 나머지 데이터로 분석 진행
df = df.dropna(subset=['upload_time'])

# 날짜를 제외하고 시간(HH:MM:SS) 정보만 추출
df['Upload_Hour_Minute'] = df['upload_time'].dt.time

# 10분 단위로 시간대별 그룹화 (시:분까지만 추출하고 10분 단위로 반올림)
df['Time_Bin'] = df['upload_time'].dt.floor('10T').dt.time

# 각 시간대별 업로드된 영상 수 계산
time_counts = df.groupby('Time_Bin').size()

# 그래프 그리기
plt.figure(figsize=(10, 6))
time_counts.plot(kind='bar', width=0.8)

# 그래프 제목과 축 레이블 설정
plt.title('Number of Video Uploads per 10-Minute Interval (Time of Day)')
plt.xlabel('Upload Time (10-minute intervals)')
plt.ylabel('Number of Videos')

# x축 레이블이 너무 많을 경우 조정
plt.xticks(rotation=45, ha='right')

# 그래프 출력
plt.tight_layout()
plt.show()

# # 선 그래프 그리기
# plt.figure(figsize=(10, 6))
# time_counts.plot(kind='line', marker='o', color='b')

# # 그래프 제목과 축 레이블 설정
# plt.title('Number of Video Uploads per 10-Minute Interval (Time of Day)')
# plt.xlabel('Upload Time (10-minute intervals)')
# plt.ylabel('Number of Videos')

# # x축 레이블이 너무 많을 경우 조정
# plt.xticks(rotation=45, ha='right')

# # 그래프 출력
# plt.tight_layout()
# plt.show()

