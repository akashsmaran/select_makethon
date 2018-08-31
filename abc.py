import csv
import matplotlib.pyplot as plt
i=0
y=[]
with open('/home/akash/Desktop/makethon1/data.csv','rb') as csvfile:
	spamreader=csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in spamreader:
		y= (y+(row))

y=map(float,y)

plt.figure('FILTERED')
plt.plot(y)
print(y)
x=len(y)
j=2
temp=[]
maxx = 0;
max_val=0
max_dat=[];
while j<x-10:
	if(y[j]>500):
		maxx=j
		max_val=y[j]
		for k in range (j-10,j+10):
			if(y[k]>max_val):
				max_val=y[k];
				maxx=k
		j=j+3		
		max_dat.append(maxx)
		plt.scatter(maxx,max_val,facecolors='red', alpha=.55, s=100)
	j+=1
j=2;

temm=0
minn = 0;
min_val=0
min_dat=[];
for g in range (0,len(max_dat)):
	minn=max_dat[g]
	min_val=y[max_dat[g]]
	for k in range(max_dat[g]-15,max_dat[g]):
		if(y[k]<min_val):
				min_val=y[k];
				minn=k
	min_dat.append(minn)
	plt.scatter(minn,min_val,facecolors='black', alpha=.55, s=100)
print(max_dat)
s = 0;
s_val=0
s_dat=[];
for g in range (0,len(max_dat)):
	s=max_dat[g]
	s_val=y[max_dat[g]]
	for k in range(max_dat[g],max_dat[g]+20):
		if(y[k]<s_val):
				s_val=y[k];
				s=k
	s_dat.append(s)
	plt.scatter(s,s_val,facecolors='green', alpha=.55, s=100)
print(s_dat)
t = 0;
t_val=0
t_dat=[];
for g in range (0,len(s_dat)):
	t=s_dat[g]
	t_val=y[s_dat[g]]
	for k in range(s_dat[g]+1,s_dat[g]+10):
		if(y[k]>t_val):
				t_val=y[k]
				t=k
	t_dat.append(t)
	plt.scatter(t,t_val,facecolors='blue', alpha=.55, s=100)
print(t_dat)

p=0
p_val=0
p_dat=[]
for h in range (0,len(min_dat)):
	p=min_dat[h]
	p_val=y[min_dat[h]]
	for k in range(min_dat[h]-25,min_dat[h]):
		if(y[k]>p_val):
				p_val=y[k];
				p=k
	p_dat.append(p)
	plt.scatter(p,p_val,facecolors='yellow', alpha=.55, s=100)

plt.ylabel('Voltage')

#r_time=[]
#for i in range (0,len(max_dat)-1):
#	r_time.append((max_dat[i+1]-max_dat[i])*0.01)
#for i in range (0,len(r_time)):
#	r_time[i]=60/r_time[i]
#print 'AVERAGE HEARTBEAT  : ' , (sum(r_time)/len(r_time)) , ' s'
#qrs_time=[]
#for i in range (0,len(max_dat)-1):
#	qrs_time.append((s_dat[i]-min_dat[i])*0.01)
#print 'AVERAGE QRS TIME  : ' , (sum(qrs_time)/len(qrs_time)*1000) , ' ms'

plt.show()
