height = input("Enter your Height in m: ")
weight = input("Enter your Weight in kg: ")
bim = int(weight) / float(height) ** 2
bim_int = int(bim)
print(bim_int)