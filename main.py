organs = [
    ["żołądek", 1.5, 2.5],
    ["dwunastnica i jelito czcze", 5.5, 7.0],
    ["jelito kręte", 6.5, 7.5],
    ["jelito ślepe", 5.5, 7.5],
    ["jelito grube i odbytnica", 6.1, 7.5]
]

try:
    ph = float(input("Podaj wartość pH: "))
    
    if ph >= 0 and ph <= 14:
        for x in organs:
            if ph >= x[1] and ph <= x[2]:
                print("Dla określonej wartości pH ustalono lokalizację kapsułki: ", x[0])

    else:
        print("Podana wartość musi zawierać się w przedziale 0-14.")
except:
    print("Podana wartość musi być liczbą.")

