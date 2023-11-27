# Safira Nur Fauziah

def buat_pola(tinggi):
    for i in range(tinggi):
        for j in range(tinggi - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("x", end="")
            if k < i:
                print("*", end="")
        print()


buat_pola(5)
