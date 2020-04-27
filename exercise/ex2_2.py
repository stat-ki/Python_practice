# Caluclate square root of x by using "for"
x = 2
rnew = x
for i in range(10):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 +r2)/2
# Printing only final result will improve execution time　(2.36E-4[sec] →　1.44E-4[sec])
print(r1, rnew, r2)