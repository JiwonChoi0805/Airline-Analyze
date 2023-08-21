import numpy as np
import matplotlib.pyplot as plt # 데이터를 그래프로 시각화 라이브러리
import pandas as pd
import seaborn as sns # 데이터 분포 시각화 라이브러리
from scipy import stats # scipy(SciPy는 과학 컴퓨팅과 기술 컴퓨팅에 사용되는 자유-오픈 소스 파이썬 라이브러리)로부터 함수를 가져오는 과학용 계산 라이브러리
from sklearn.datasets import load_boston # 사이킷런 데이타셋

import warnings
warnings.filterwarnings('ignore') # 경고무시

# boston 데이타셋 로드
boston=load_boston()

# boston 데이타셋 DataFrame 변환
df=pd.DataFrame(boston.data, columns=boston.feature_names)

# target array로 주택가격(price)을 추가함
df['PRICE']=boston.target
print('Boston 데이타셋 크기:', df.shape)
df.head(2)


# 2x4 subplot(부플롯) 이용, axs는 4x2
fig, axs = plt.subplots(figsize=(16,8), ncols=4, nrows=2)
lm_features=['RM', 'ZN', 'INDUS', 'NOX', 'AGE', 'PTRATIO', 'LSTAT', 'RAD']

#i에는 인덱스가 feature에는 RM~RAD까지 순차적으로 들어감
#enumerate() 함수:세다, 열거하다/ 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 객체를 리턴함
for i, feature in enumerate(lm_features):
  row=int(i/4) #2행
  col=i%4
  
  #sns.regplot : 회귀직선을 그려줌
  sns.regplot(x=feature, y='PRICE', data=df, ax=axs[row][col])


