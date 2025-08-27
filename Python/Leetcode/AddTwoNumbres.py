
a = [9, 9, 9]
b = [1]
c = []

a.reverse()
b.reverse()

residue = 0
max_len = max(len(a), len(b))

for i in range(max_len):
    digit_a = a[i] if i < len(a) else 0
    digit_b = b[i] if i < len(b) else 0
    
    suma = digit_a + digit_b + residue
    c.append(suma % 10)
    residue = suma // 10

if residue:
    c.append(residue)

c.reverse()
print(c)







