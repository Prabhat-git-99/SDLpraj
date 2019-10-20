from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
# Create your views here.
def home(request):
    return render(request,'home.html')
def create(request):
    return render(request,'create.html')
def login(request):
    return render(request,'login.html')
def ch(request):
    return render(request,'check.html')
def cr(request):
    return render(request,'crop.html')
def fert(request):
    return render(request,'fer.html')
def fun(request):
    return render(request,'offer.html') 

def input(request):
  # na = data.amt
  if 'Fname' in request.POST:
    first_name = request.POST['Fname']
  else:
    first_name = False

  if 'Lname' in request.POST:
    last_name = request.POST['Lname']
  else:
    last_name = False

  if 'uname' in request.POST:
    usern = request.POST['uname']
  else:
    usern = False
  
  if 'pass' in request.POST:
    pw = request.POST['pass']
  else:
    pw = False

  if 'addr' in request.POST:
    addrs = request.POST['addr']
  else:
    addrs = False

  if 'contactN' in request.POST:
    cont = request.POST['contactN']
  else:
    cont = False

  if 'mail' in request.POST:
    em = request.POST['mail']
  else:
    em = False

  if 'dob' in request.POST:
    birth = request.POST['dob']
  else:
    birth = False

  if 'loanamt' in request.POST:
    Amt =int(request.POST['loanamt'])
  else:
    Amt = False
  #data = pd.read_csv('Book1.csv')
  u=[usern]
  fn=[first_name]
  ln=[last_name]
  ad=[addrs]
  db=[birth]
  e=[em]
  cno=[cont]
  no=[Amt]
  p=[pw]
  dict = {'FirstName':fn,'LastName':ln,'address':ad,'contact':cno,'email':e,'birthdate':db,'loan':no}
  df = pd.DataFrame(dict)
  with open('Book1.csv','a') as f:
    df.to_csv(f,header=False,index=False)
  dict ={'USERNAME':u,'PASSWORD':p}
  df=pd.DataFrame(dict)
  with open('login.csv','a') as n:
    df.to_csv(n,header=False,index=False)
  if(Amt > 500000):
    return render(request,'offer.html',{'name':first_name,'l':last_name,'e':"eligible"})
  else:
    return render(request,'not.html',{'name':first_name})
    # return render(request,'result.html',{'eligible':"Not Eligible",'First_name':first_name,'Last_name':last_name})  
def log_data(request):
  if 'uname' in request.POST:
    username=request.POST['uname']
  else:
    username=False
  if 'pass' in request.POST:
    pw=request.POST['pass']
  else:
    pw=False
  
  data = pd.read_csv('login.csv')
  na = data['USERNAME']
  f=0
 
  for i in data:
    #if i==username:
    ref = data[data.USERNAME == username]
    refp = data[data.PASSWORD == str(pw)]
    if (len(ref)!=0 and len(refp)!=0): 
    #if((data['USERNAME']==username) and (int(data['PASSWORD'])==int(pw))):
      #p=data.readline()
      f=1
      break
    else:  
      f=0
   #return render(request,'result.html',{'f':i,'p':pw})
  if f==1: 
    return render(request,'offer.html',{'name':username})
  else:
     return render(request,'login.html')  

def check(request):
  
  data=pd.read_csv('Book1.csv')
  na=data['loan']
  ch = "JE::EL:LKLKLD:"
  cnt=[]
  '''for i in na:
    j=0

    cnt[j]=cnt+1
    j=j+1'''
  cnt1=0
  cnt2=0
  names=['>3','>5']
  #plt.plot(cnt,na)
  #plt.show()
  a=1
  for i in na:
      if i<50000:
        cnt1=cnt1+1
      else:
        cnt2=cnt2+1
  cnt3=[cnt1,cnt2]
  plt.bar(names,cnt3)
  plt.show()
  #return render(request,'check.html',{'c1':ch,'c2':cnt2,'c3':ch})                   