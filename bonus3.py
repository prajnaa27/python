password = input("Enter a password\n")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper"] = upper

print(result)

# all returns true only if all the elements in the list is true(for boolean entries only)
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")