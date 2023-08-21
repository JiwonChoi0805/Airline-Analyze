## 항공권 분석 (2023.1~2023.02)

### 분석의 목표

1.이착륙 시간대에 따라 항공권 가격이 영향을 받는가? <br/>
departure_time - price <br/>
arrival_time - price <br/>
 <br/>
Early Morning : 5:00이상 - 8:00미만 <br/>
Morning: 8:00이상 - 12:00미만 <br/>
Afternoon: 12:00이상 - 17:00미만 <br/>
Evening: 17:00 이상 - 21:00미만 <br/>
Night: 이상 21:00이상 - 24:00 미만 <br/>
Late Night: 00:00이상 - 5:00 미만 <br/>
 <br/>
2.출발일에 임박하여 사는 항공권이 더 비싼가? days_left - price <br/>
3.출발공항에 따라 항공권 가격이 어떻게 다를까? source_airport - price <br/>


### 데이타셋
편명 <br/>
출발지 공항  <br/>
도착지 오사카 <br/>
도착일-예약일 <br/>
출발시간 <br/>
도착시간 <br/>
가격 <br/>

### 참고
https://blog.naver.com/lilyan0917/222791574683  <br/>
https://www.kaggle.com/code/tunaeem/flight-price-prediction-eda-linear-regression
