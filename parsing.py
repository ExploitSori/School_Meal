import urllib
import BeautifulSoup
import re
from datetime import datetime

week = ['��', 'ȭ', '��', '��', '��', '��', '��']
school="input your school code"

url="http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode="+school+"&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=1"
html=urllib.urlopen(url)
pas=BeautifulSoup.BeautifulSoup(html)
paslist=pas.findAll('td')
t=datetime.today().weekday()+1#�޽� ���̺��� ù�� �Ͽ����� 0 ������ weekday �Լ��� �������� 0
day=datetime.today().day#���� ��¥ +������ ������� ���̺��� �Ĵ�ǥ�� �Ľ�

result=str(paslist[t+day])

print str(datetime.today().year)+"�� "+str(datetime.today().month)+"�� "+str(day)+"�� "+week[t-1]+"����"

foodlist=re.split('<br />',result)
del foodlist[0]
del foodlist[0]

for i in foodlist:
    food=i
    sli=food.find('*')#*�������� �����̽�
    print food[:sli]

