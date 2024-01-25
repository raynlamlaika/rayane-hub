import numpy as np


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,1,1],[1,10,1],[1,1,1]]

array=np.array([100,200,300,400,500])
print ('array[matrix]   ' ,array)

print ('num.py its here')
ra = np.arange(0,20,)
# 0 = debut 20 = la fin 3 = the steep 
print(ra)
syy= ra.shape
# to kmow shep of matrix 
print('THE SHEPPPPPPPPPP ITS ',syy)
print("\n")

z = np.zeros(3)
print (z)
#all = 0 

print("\n")

a = np.ones(5)
ftt= np.ones(( 2,3))
print (ftt)
print (a)
# all =  1

print("\n")

gat = np.random.randint (5 ,9, 8)
shape = gat.reshape(4,2)
print (shape)
#to reshape the mitrix l dakchi li b4iti and numbre in matrikc == a*b in reshape

print("\n")

gpt = np.random.randint( 11,2000, (3,6))
print (gpt)
# we can do it like a matrix  

maximum = gpt.max()
print ('\n')
print ("maximum : " + str (maximum))
#to get from te matrix maximum numbree

print("\n")
minimum = gpt.min()
print ('\n')
print ("minimum : " + str (minimum))
#to get from te matrix minimum numbree 


print("\n")
myy = gpt.argmax()
mtt = gpt.argmin()

print('indexx max :' +str (myy))
print('index mini :' +str (mtt))
# to index min ot max numbre



gat_fasila = np.random.rand(2 ,3)
# we can add anthor nomber to give the nmbress need
print (gat)
print( gat_fasila)
# to importy ramndo,m romre for tha () 

print("\n")


nn = np.arange(1,11)
np.random.shuffle(nn)
print (nn)
#to mike all nombres random

print("\n")

nnsh = nn.reshape(2,5)
print('HHHHHHHH',nnsh)

print("\n")

#we can do it in matrix
np.random.shuffle(nnsh)
print (nnsh)

typ = np.random.randint( 11,2000, (3,6))
print (typ)
print ('\n')


styp = typ.shape
rtyp = typ.shape[0]
ctyp = typ.shape[1]
# to know sep of matrix  1 = columns and 0 = row
print('the shep of this matrix is : ' + str(styp))
print('the columns of this matrix is : ' + str(ctyp))
print('the rows of this matrix is: ' + str(rtyp))

print ('\n')
tcc =np.ceil(2.1)
print (tcc)
#ceil its 7ayad virgol o dir akbar 3adad

print("\n")
fll= np.floor(2.4)
print ( fll)
#floor its to delet virgool

r1 = np.round(2.4)
r2 = np.round(9.7)
#to get most colose numbre
print('ytdfxfg',r1)
print(r2)

print('\n')
add = np.add(2,34)
print(add)
# to add 

add2= np.add(matrix,2)
print(add2) #add in matrix
add3 = np.add(matrix , matrix2)
print (add3) #to add to matrix condition its shape1 = shape2      

print ('\n')

mul = np.multiply(matrix,7)
print ('mutply :' , mul)
#to multiply matrixx and you can do t in too matrix
print('\n')

div = np.divide(matrix,matrix2)
print(div)
# to divide to nubre or matrix ...

Tyu=np.eye(7)
print(Tyu)
print('\n')
print ('finisiooooooooooo smat ratt att ')


fddd='12/20/12/20'
print(fddd.split('/')[3])

#chech type its the same []if type =samee===True
olk=isinstance(23,int)
olk3=isinstance(['wrg' '2trgw' 'wtgw5'], object)
print(olk,olk3)
olk55=isinstance(234,(float ,int ,str))
print(olk55)