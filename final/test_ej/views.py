from django.shortcuts import render
from django.http import HttpResponse

# def index1(request):
    #return HttpResponse('<u>Hello</u>')


#import csv
#import pandas as pd
#from test_ej.models import hospital
#with open('C:/Users/user/Desktop/final/자료/hospital.csv','rt', encoding='UTF-8') as f:
#    dr = csv.DictReader(f)
#    s = pd.DataFrame(dr)
#ss = []
#for i in range(len(s)):
#    st = (s['ID'][i], s['병원/약국명'][i], s['병원/약국구분'][i], s['전화번호'][i], s['우편번호'][i], s['소재지주소'][i])
#    ss.append(st)
#for i in range(len(s)):
#    hospital.objects.create(id=ss[i][0], name=ss[i][1], sep=ss[i][2], tel=ss[i][3], zip=ss[i][4], add=ss[i][5])