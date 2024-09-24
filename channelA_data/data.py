import pandas as pd
import os

# 현재 작업 디렉토리 기준으로 파일 경로 설정
excel_file_paths = [f"data/2023년{i}월 고정형 TV 실시간 시청기록 기초데이터(장르시트추가).xlsx" for i in range(1, 13)]

# 필터링 패턴
pattern = '선넘은패밀리(본)'

def filter_data_from_excel(file_path):
    try:
        # 엑셀 파일에서 "프로그램월평균리스트" 시트를 읽음, 처음 7줄을 건너뛰고 읽기
        df = pd.read_excel(file_path, sheet_name='프로그램월평균리스트', skiprows=7)
        
        # 새 컬럼 이름 리스트
        new_column_names = ['번호', '프로그램명', '장르', '채널', '개인 전체 시청시간', '개인 전체 시청률',
                            '4-9세 남자 시청시간', '4-9세 남자 시청률', '4-9세 여자 시청시간', '4-9세 여자 시청률',
                            '10대 남자 시청시간', '10대 남자 시청률', '10대 여자 시청시간', '10대 여자 시청률',
                            '20대 남자 시청시간', '20대 남자 시청률', '20대 여자 시청시간', '20대 여자 시청률',
                            '30대 남자 시청시간', '30대 남자 시청률', '30대 여자 시청시간', '30대 여자 시청률',
                            '40대 남자 시청시간', '40대 남자 시청률', '40대 여자 시청시간', '40대 여자 시청률',
                            '50대 남자 시청시간', '50대 남자 시청률', '50대 여자 시청시간', '50대 여자 시청률',
                            '60대 이상 남자 시청시간', '60대 이상 남자 시청률', '60세 이상 여자 시청시간', '60대 여자 시청률']
        
        # 컬럼 이름을 새로 지정하기 전에 컬럼 수 일치 확인
        if len(df.columns) == len(new_column_names):
            df.columns = new_column_names
        else:
            print(f"Column mismatch in file {file_path}")
            return pd.DataFrame()  # 컬럼 수 불일치 시 빈 DataFrame 반환
        
        # 필터링 (정규 표현식 사용)
        filtered_df = df[df['프로그램명'].str.contains(pattern, na=False, regex=True)]
        
        if filtered_df.empty:
            print(f"No matching data in file {file_path}")
        
        return filtered_df
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return pd.DataFrame()  # 오류 발생 시 빈 DataFrame 반환

# 필터링된 데이터의 CSV 파일 저장 및 병합
all_filtered_dfs = []

for file_path in excel_file_paths:
    full_path = os.path.join(os.getcwd(), file_path)
    if os.path.exists(full_path):
        filtered_data = filter_data_from_excel(full_path)
        if not filtered_data.empty:
            # 결과를 CSV 파일로 저장
            # output_file = os.path.join(os.getcwd(), f"filtered_{os.path.basename(file_path).replace('.xlsx', '.csv')}")
            try:
                filtered_data.to_csv(output_file, index=False, encoding='utf-8-sig')
                all_filtered_dfs.append(filtered_data)
            except Exception as e:
                print(f"Error saving CSV for {file_path}: {e}")
    else:
        print(f"File not found: {full_path}")

# 모든 필터링된 데이터를 병합
if all_filtered_dfs:
    combined_df = pd.concat(all_filtered_dfs, ignore_index=True)
    # 최종 결과를 CSV 파일로 저장
    output_combined_file = os.path.join(os.getcwd(), "선넘은패밀리_2023.csv")
    try:
        combined_df.to_csv(output_combined_file, index=False, encoding='utf-8-sig')
    except Exception as e:
        print(f"Error saving combined CSV: {e}")
else:
    print("No data to combine.")