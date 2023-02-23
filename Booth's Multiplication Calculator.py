from tabulate import tabulate as tb
from fpdf import FPDF


def dectobin(num):
    a = bin(num).replace("0b","")
    if len(str(a)) < 4:
        a = str(a).zfill(4)
        return a
    else:
        return a 

def tcomplement(neg):
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

def ficbit(x):
    q = str(x) + '0'
    return q 

def ars(x, y):
    l1 = [i for i in x]
    l2 = [i for i in y]
    l1 += l2 
    #print(l1)
    b = ''.join(l1)
    #print(b)
    num = int(b, 2)
    num = num >> 1
    c = bin(num).replace("0b","")
    #print(c)
    if l1[0] == '0':
        c = str(c).zfill(len(b))
        return c 
    elif l1[0] == '1':
        z = '1' * (len(b)-len(str(c)))
        c = z + c
        return c

def ad(x, y):
    l = bin(int(x, 2) + int(y, 2)).replace("0b", "")
    return l 

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

print("\nBooth's Multiplication Calculator\n")

a,b = map(int, input("Enter the nos.: ").split())
M = dectobin(a) if a > 0 else tcomplement(a)
Q = dectobin(b) if b > 0 else tcomplement(b)

#initialize the accumulator.
A = '0' * len(str(M))
size = len(str(Q))
#print(size)

#bits in A & Q
a_bit = len(str(A))
q_bit = len(str(Q))
#print(a_bit)
#print(q_bit)

#adding the fictious bit to Q.
Qf = ficbit(Q)
#print(Qf)
qf_bit = len(str(Qf))


data = [['Initial', M, A, Qf, size]]
#print(data)


#iteration for steps.
while(size!=0):
    size -= 1

    if (Qf[-2:] == '00'): 
        z = ars(A, Qf)
        A = z[:a_bit]
        Qf = z[-qf_bit:]

        calc_data = ['Q[0]=0 & Q[-1]=0 ARS(AQ)', str(M), str(A), str(Qf), size]
        data.append(calc_data)

    elif (Qf[-2:] == '11'):
        z = ars(A, Qf)
        A = z[:a_bit]
        Qf = z[-qf_bit:]

        calc_data = ['Q[0]=1 & Q[-1]=1 ARS(AQ)', str(M), str(A), str(Qf), size]
        data.append(calc_data)

    elif (Qf[-2:] == '01'):
        A = ad(A, M)

        calc_data = ['Q[0]=0 & Q[-1]=1 A=A+M', str(M), str(A), str(Qf), '-']
        data.append(calc_data)

        z = ars(A, Qf)
        A = z[:a_bit]
        Qf = z[-qf_bit:]

        calc_data = ['ARS(AQ)', str(M), str(A), str(Qf), size]
        data.append(calc_data)

    elif (Qf[-2:] == '10'):
        A = sb(A, M)
        #print(A)

        calc_data = ['Q[0]=1 & Q[-1]=0 A=A-M', str(M), str(A), str(Qf), '-']
        data.append(calc_data)

        z = ars(A, Qf)
        #print("z=", z)
        A = z[:a_bit]
        #print('A=', A)
        Qf = z[-qf_bit:]
        #print('Qf =', Qf)

        calc_data = ['ARS(AQ)', str(M), str(A), str(Qf), size]
        data.append(calc_data)

#result calculation
l1 = [i for i in A]
l2 = [i for i in Qf]
l1 += l2
r_bit = a_bit + q_bit
res_join = ''.join(l1)
result = res_join[:r_bit]


print("\n")


print('M =', a, " =", M)
print('Q =', b, " =", Q)
#print(data)
print("\n")

print(tb(data, headers=["Operation", "M", "A", "Q", "Size"]))
print("The result is: ", result)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 12)
pdf.set_margins(left=10, top=100, right=20)

pdf.cell(70, 10, "Booth's Multiplication Calculator")
pdf.ln()

pdf.cell(10, 10, 'M = ')
pdf.cell(10, 10, str(a))
pdf.cell(5, 10, '=')
pdf.cell(10, 10, str(M))
pdf.ln()

pdf.cell(10, 10, 'Q = ')
pdf.cell(10, 10, str(b))
pdf.cell(5, 10, '=')
pdf.cell(10, 10, str(Q))
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

pdf.cell(30, 10, 'The result is =')
pdf.cell(30, 10, str(result))
pdf.ln()

pdf.output("Booth's.pdf")
