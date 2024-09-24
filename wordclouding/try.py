import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager

# CSV 파일 읽기
file_path = 'keyword.csv'  # 파일 경로 지정
df = pd.read_csv(file_path)

# 한글 폰트 설정 (Windows에서 Malgun Gothic 폰트를 사용)
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# '요일' 칼럼에서 '목'과 '금'으로 필터링
for day in ['목', '금']:
    filtered_df = df[df['요일'] == day]

    # '장르' 칼럼만 추출하여 텍스트로 변환
    genre_text = ' '.join(filtered_df['장르'].astype(str))

    # 워드 클라우드 생성 (폰트 설정 추가)
    wordcloud = WordCloud(
        font_path=font_path,  # 폰트 경로 추가
        width=800, 
        height=400, 
        background_color='white'
    ).generate(genre_text)

    # 워드 클라우드 시각화
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'{day}요일 장르 워드 클라우드')
    plt.show()
