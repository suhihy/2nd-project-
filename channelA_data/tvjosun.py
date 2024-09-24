import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('TV조선_2023.csv')

# '번호' 열 삭제
df = df.drop(columns=['번호'])

# 줄 번호 생성
df['줄번호'] = ((df.index // 2) + 1).astype(str)

# '프로그램명' 열에 줄 번호 추가
df['프로그램명'] = df['줄번호'] + '/' + df['프로그램명']

# '줄번호' 열 삭제
df = df.drop(columns=['줄번호'])

# 수정된 데이터를 새로운 CSV 파일로 저장
df.to_csv('TV조선2023_data.csv', index=False)
