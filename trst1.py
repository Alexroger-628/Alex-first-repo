# get the input
m = int(input("Type in the first number: "))
n = int(input("Type in the second number: "))
# calculate m!, n!, (m-n)!
fm = 1
for i in range(1, m + 1):
    fm *= i
print(fm)
fn = 1
for i in range(1, n + 1):
    fn *= i
print(fn)
fmn = 1
for i in range(1, m - n + 1):
    fmn *= i
print(fmn)
# get the answer
print(fm // fn //fmn) 
