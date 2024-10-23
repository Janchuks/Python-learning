print("Valūtas maiņa")
curv = input("Kādu valūtu vēlaties mainīt? USD, GBP, CNY, JPY, CAD, AUD: ").upper()
uzcur = input("Uz kādu valūtu vēlaties mainīt? USD, GBP, CNY, JPY, CAD, AUD: ").upper()

valutasrateeuro = {
    "USD": 0.93506,
    "GBP": 1.1677025,
    "CNY": 0.1290521,
    "JPY": 0.0059145,
    "CAD": 0.683448,
    "AUD": 0.610968
}

nauda = float(input("Ievadiet summu, kuru vēlaties konvertēt: "))

# Pārbauda, vai valūtas ir atbalstītas un ja nepieciešams, iziet
if curv not in valutasrateeuro or uzcur not in valutasrateeuro:
    print("Nederīga valūta!")
elif curv == uzcur:
    print(f"{nauda} {curv} ir tā pati summa pēc apmaiņas.")
else:
    excnauda = nauda * (valutasrateeuro[curv] / valutasrateeuro[uzcur])
    print(f"{nauda} {curv} pēc apmaiņas ir {excnauda} {uzcur}.")
