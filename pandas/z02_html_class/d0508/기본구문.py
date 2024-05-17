import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
df

df.head() # 상위 5개
df.tail() # 하위 5개
df.describe()  #컬럼별 최소 최대값 등 대략적인 정보
df.info() # 컬럼별 타입 크기 정보
df.values  # rows 데이터 배열로 출력
df.index  # index 정보
df.shape # 데이터 크기 정보
df.columns  # 컬럼 정보

df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name= '지원번호'
df.sort_index(inplace=True)
df.to_csv('score.csv',encoding='utf-8')

df['이름']
df.columns
df.columns[0]
df['이름']
df[df.columns[0]]  # == df['이름']
df[df.columns[-1]]  #제일 마지막 컬럼의 데이터

df['학교'].unique() #중복제거 한 후에 학교이름 출력
df['학교'].nunique()  #중복 제거 한후 갯수 출력

df[0:3]
df[5:]
df.iloc[[0,1,3]]