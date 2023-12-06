import matplotlib.pylab as plt
import numpy as num
#AMPLITUDE SHIFT KEYING.....................
F1=10 
F2=2 
A=5
t=num.arange(0,1,0.001)
x=A*num.sin(2*num.pi*F1*t)
u=[]
b=[0.2,0.4,0.6,0.8,1.0]

s=1
for i in t:
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
       
    u.append(s)
v=[]
for i in range(len(t)):
    v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])
    
plt.subplot(3,3,1)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier')
plt.grid(True)

plt.subplot(3,3,4)
plt.plot(t,u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)

plt.subplot(3,3,7)
plt.plot(t,v)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ASK Signal')
plt.grid(True)
plt.tight_layout()


# FREQUENCY SHIFT KEYING............................

t=num.arange(0,1,0.001)
x=A*num.sin(2*num.pi*F1*t)
 
plt.subplot(3,3,2)
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("Carrier")
plt.grid(True)

u=[]
b=[0.2,0.4,0.6,0.8,1.0]
s=1
for i in t:
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
    u.append(s)

plt.subplot(3,3,5)
plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)

v=[]
for i in range(len(t)):
    if(u[i]==1):
        v.append(A*num.sin(2*num.pi*F1*t[i]))
    else:
        v.append(num.sin(2*num.pi*F1*t[i])*-1)

plt.subplot(3,3,8)
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("FSK")
plt.grid(True)
plt.tight_layout()



#PHASE SHIFT KEYING................................

t=num.arange(0,1,0.001)
x=A*num.sin(2*num.pi*F1*t)

plt.subplot(3,3,3)
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("Carrier")
plt.grid(True)

u=[]
b=[0.2,0.4,0.6,0.8,1.0]
s=1
for i in t: 
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
    u.append(s)

plt.subplot(3,3,6)
plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)

v=[]
for i in range(len(t)):
    if(u[i]==1):
        v.append(A*num.sin(2*num.pi*F1*t[i]))
    else:
        v.append(A*num.sin(2*num.pi*F1*t[i])*-1)

plt.subplot(3,3,9)
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("PSK")
plt.grid(True)
plt.tight_layout()
plt.show()
