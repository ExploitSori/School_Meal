import urllib
import BeautifulSoup
import re
from datetime import datetime

week = ['월', '화', '수', '목', '금', '토', '일']
school="input your school code"

url="http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode="+school+"&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=1"
html=urllib.urlopen(url)
pas=BeautifulSoup.BeautifulSoup(html)
paslist=pas.findAll('td')

t=datetime.today().weekday()+1#급식 테이블은 첫주 일요일이 0 하지만 weekday 함수는 월요일이 0
day=datetime.today().day#오늘 날짜 +요일을 더해줘야 테이블의 식단표를 파싱

weeks=day/7
y=weeks*7
x=t

result=str(paslist[y+x])

print str(datetime.today().year)+"년 "+str(datetime.today().month)+"월 "+str(day)+"일 "+week[t-1]+"요일"

foodlist=re.split('<br />',result)
del foodlist[0]
del foodlist[0]

for i in foodlist:
    food=i
    sli=food.find('*')#*기준으로 슬라이스
    print food[:sli]
