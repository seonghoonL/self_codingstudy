pepper_shu = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
n = int(input())
t = sum(pepper_shu[input()] for _ in range(n))
print(t)