print("Bonjou")
print("Byenvini sou pwogram 'Grade Calculator'. Nou kalkile nòt so 100\n")
nonb_not = input("Ki kantite nòt ou pral antre: ")
not_yo = []

while not nonb_not.isdigit():
    nonb_not = input("Ki kantite nòt ou pral antre: ")
nonb_not = int(nonb_not)

for n in range(nonb_not):
    yon_not = float(input(f"Antre nòt nimewo {n+1} an: "))
    not_yo.append(yon_not)
mwayen = round(sum(not_yo)/nonb_not, 2)
print()
if mwayen >= 90:
    print(f"Ou fè mwayèn {mwayen}, klasifikasyon 'A'")
elif mwayen < 90 and mwayen >= 80:
    print(f"Ou fè mwayèn {mwayen}, klasifikasyon 'B'")
elif mwayen < 80 and mwayen >= 70:
    print(f"Ou fè mwayèn {mwayen}, klasifikasyon 'C'")
elif mwayen < 70 and mwayen >= 60:
    print(f"Ou fè mwayèn {mwayen}, klasifikasyon 'D'")
else:
    print(f"Ou fè mwayèn {mwayen}, klasifikasyon 'F'")
