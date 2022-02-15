import numpy as np
import random
import math


def logic(a,num,vlo):
	for i in range(3):
		if a[i][0]==a[i][1]==a[i][2]==2 or a[0][i]==a[1][i]==a[2][i]==2 or a[0][0]==a[1][1]==a[2][2]==2 or a[-1][0]==a[-2][1]==a[-3][2]==2:
			print('Выйграл О')
			return 1
		elif a[i][0]==a[i][1]==a[i][2]==3 or a[0][i]==a[1][i]==a[2][i]==3 or a[0][0]==a[1][1]==a[2][2]==3 or a[-1][0]==a[-2][1]==a[-3][2]==3:
			print('Выйграл Х')	
			return 1
		elif num>=9:
			print('Ничья')
			return 1



def xod(m,znak):
	x=math.ceil(m/3)-1
	y=m-3*x-1
	global pole
	if pole[x][y]==0:
		pole[x][y]=znak
		screen(pole)
		return 0
	else:
		print('Эта клетка уже занята!')
		return 1
	
def screen(pole):
	for i in range(3):
		for j in range(3):
			if pole[i][j]==0:
				print(3*i+j+1,end=' ')
			elif pole[i][j]==2:
				print('O',end=' ')
			if pole[i][j]==3:
				print('x',end=' ')
		print()
			
	
def xto():
	global kto
	l=1
	if kto==2:
		while l:
			xy=int(input())
			l=xod(xy,2)
		kto+=1
	elif kto==3:
		while l:
			xy=int(input())
			l=xod(xy,3)
		kto-=1


if __name__=="__main__":
	pole=np.zeros((3,3))
	o=2
	x=3
	kto=random.randint(2,3)
	num_xod=0
	while 1:
		xto()
		num_xod+=1
		if logic(pole,num_xod,kto):
			break	