import sys

# โจทย์ระบุว่าถ้ามี argument (len > 1) ให้ปริ้น none
if len(sys.argv) > 1:
    print("none")
else:
    x = 0
    while x <= 10:
        print(f"Table de {x}:", end=" ")
        j = 0
        while j <= 10:
            print(x * j, end=" ")
            j += 1
        print()
        x += 1