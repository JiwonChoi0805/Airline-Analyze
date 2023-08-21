## 항공권 분석 (2023.1~2023.02)

### 분석의 목표

1. 이착륙 시간대에 따라 항공권 가격이 영향을 받는가? 
departure_time - price
arrival_time - price

Early Morning : 5:00이상 - 8:00미만
Morning: 8:00이상 - 12:00미만
Afternoon: 12:00이상 - 17:00미만
Evening: 17:00 이상 - 21:00미만
Night: 이상 21:00이상 - 24:00 미만
Late Night: 00:00이상 - 5:00 미만

2. 출발일에 임박하여 사는 항공권이 더 비싼가? days_left - price

3. 출발공항에 따라 항공권 가격이 어떻게 다를까? source_airport - price


### 데이타셋
편명
출발지 공항 
도착지 오사카
도착일-예약일
출발시간
도착시간
가격

### 참고
https://blog.naver.com/lilyan0917/222791574683
https://www.kaggle.com/code/tunaeem/flight-price-prediction-eda-linear-regression
