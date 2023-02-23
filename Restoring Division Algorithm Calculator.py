from tabulate import tabulate as tb
from fpdf import FPDF


def dectobinq(num):
    a = bin(num).replace("0b","")
    if len(str(a)) < 4:
        a = str(a).zfill(4)
        return a
    else:
        return a 

def dectobinm(num):
    a = bin(num).replace("0b","")
    a = str(a).zfill(q_bit+1)
    return a
    #else:
        #return a 


#def tcomplement(neg):
    a = bin(neg).replace("0b","")
    num = str(a).zfill(4) if len(str(a)) < 4 else str(a).zfill(1 + len(str(a)))
        #print(num)
    
    lst = []
    for i in num:
        if i == '1':
            lst.append(str(0))
        elif i == '0':
            lst.append(str(1))
    b = ''.join(lst)
    complement = bin(int(b, 2) + int("1", 2)).replace("0b","")
    return complement

def tcomp(x):
    lst = [str(1) if i == '0' else str(0) for i in x]
    b = ''.join(lst)
    complement = bin(int(b, 2) + int("1", 2)).replace("0b","")
    return str(complement).zfill(len(b)) if len(str(complement)) < len(b) else str(complement)

def als(x, y):
    l1 = [i for i in x]
    l2 = [i for i in y]
    l1 += l2 
    #print(l1)
    b = ''.join(l1)
    #print(b)
    num = int(b, 2)
    num = num << 1
    c = bin(num).replace("0b","")
    #print(c)
    if l1[0] == '0':
        c = str(c).zfill(len(b))
        c = c[:-1] + "_"
        return c 
    #elif l1[0] == '1':
        z = '1' * (len(b)-len(str(c)))
        c = z + c
        return c

def sb(x, y):
    z = tcomp(y)
    #print("z=", z)
    l = bin(int(x, 2) + int(z, 2)).replace("0b","")
    if len(str(l)) < len(str(x)):
        l = str(l).zfill((len(str(x))))
        #print(l)
        return l 
    elif len(str(l)) > len(str(x)):
        l = l[-a_bit:]
        return l
    else:
        return l 




print("\nRestoring Division Algorithm Calculator\n")

a,b = map(int, input("Enter the nos.: ").split())
Q = dectobinq(a) #if a > 0 else tcomplement(a)
q_bit = len(str(Q))
Qf = Q 

M = dectobinm(b) #if b > 0 else tcomplement(b)

#initialize the accumulator.
A = '0' * len(str(M))
size = len(str(Q))
#print(size)

#bits in A & Q
a_bit = len(str(A))

#print(a_bit)
#print(q_bit)

#adding the fictious bit to Q.
#Qf = ficbit(Q)
#print(Qf)
#qf_bit = len(str(Qf))

print('Q =', a, " =", Qf)
print('M =', b, " =", M)
#print(data)
print("\n")


data = [['Initial', M, A, Q, size]]
#print(data)

while(size!=0):
    size -= 1

    z = als(A, Q)
    A = z[:a_bit]
    Q = z[q_bit+1:]

    calc_data = ['ALS(AQ)', str(M), str(A), str(Q), '-']
    data.append(calc_data)

    A1 = sb(A, M)
    calc_data = ['A=A-M', str(M), str(A1), str(Q), '-']
    data.append(calc_data)

    if (A1[0] == '0'): 
        Q = Q[:-1] + "1"
        A = A1
        calc_data = ['As sign of A +ve; Q[0]=1', str(M), str(A), str(Q), size]
        data.append(calc_data)

    elif (A1[0] == '1'):
        Q = Q[:-1] + "0"
        calc_data = ['As sign of A -ve; Q[0]=0', str(M), str(A1), str(Q), '-']
        data.append(calc_data)

        calc_data = ['Restore A', str(M), str(A), str(Q), size]
        data.append(calc_data)
    

#result calculation
l1 = [i for i in A]
l2 = [i for i in Q]
l1 += l2
r_bit = a_bit + q_bit
res_join = ''.join(l1)
result = res_join[:r_bit]


#print("\n")



print(tb(data, headers=["Operation", "M", "A", "Q", "Size"]))
print("The quotient is: ", Q)
print("The remainder is: ", A)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 12)
pdf.set_margins(left=10, top=100, right=20)

pdf.cell(70, 10, "Restoring Division Algorithm Calculator")
pdf.ln()

pdf.cell(10, 10, 'Q = ')
pdf.cell(10, 10, str(a))
pdf.cell(5, 10, '=')
pdf.cell(10, 10, str(Qf))
pdf.ln()

pdf.cell(10, 10, 'M = ')
pdf.cell(10, 10, str(b))
pdf.cell(5, 10, '=')
pdf.cell(10, 10, str(M))
pdf.ln()
pdf.ln()

pdf.cell(70, 10, 'Operation', border=1)
pdf.cell(30, 10, 'M', border=1)
pdf.cell(30, 10, 'A', border=1)
pdf.cell(30, 10, 'Q', border=1)
pdf.cell(20, 10, 'Size', border=1)
pdf.ln()

for row in data[0:]:
    op, m, a_, q, s = row
    pdf.cell(70, 10, op, border=1)
    pdf.cell(30, 10, str(m), border=1)
    pdf.cell(30, 10, str(a_), border=1)
    pdf.cell(30, 10, str(q), border=1)
    pdf.cell(20, 10, str(s), border=1)
    pdf.ln()

pdf.ln()

pdf.cell(40, 10, 'The quotient is =')
pdf.cell(30, 10, str(Q))
pdf.ln()

pdf.cell(40, 10, 'The remainder is =')
pdf.cell(30, 10, str(A))
pdf.ln()

pdf.output('Restoring.pdf')
