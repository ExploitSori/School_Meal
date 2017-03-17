import urllib
import BeautifulSoup
import re
from datetime import datetime

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
school="B100000662"

url="http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode="+school+"&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=1"
html=urllib.urlopen(url)
pas=BeautifulSoup.BeautifulSoup(html)
paslist=pas.findAll('td')

t=datetime.today().weekday()+1
day=datetime.today().day
weeks=day/7
y=weeks*7
x=t

result=str(paslist[y+x])

print str(datetime.today().year)+"-"+str(datetime.today().month)+"-"+str(day)+"-"+week[t-1]

foodlist=re.split('<br />',result)
try:
    del foodlist[0]
    del foodlist[0]
except:
    print "To day is holyday"
for i in foodlist:
    food=i
    sli=food.find('*')
    print food[:sli]
