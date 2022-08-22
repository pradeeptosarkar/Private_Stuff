def net_income(n):
    total_tax = 0

    if n > 250_000 and n <= 500_000:
        total_tax = int(0.05 * (n - 250_000))

    elif n > 500_000 and n <= 750_000:
        total_tax = int(0.1 * (n - 500_000))
        total_tax += slab_steps['2']

    elif n > 750_000 and n <= 1_000_000:
        total_tax = int(0.15 * (n - 750_000))
        total_tax += slab_steps['3']

    elif n > 1_000_000 and n <= 1_250_000:
        total_tax = int(0.2 * (n - 1_000_000))
        total_tax += slab_steps['4']

    elif n > 1_250_000 and n <= 1_500_000:
        total_tax = int(0.25 * (n - 1_250_000))
        total_tax += slab_steps['5']

    elif n > 1_500_000:
        total_tax = int(0.3 * (n - 1_500_000))
        total_tax += slab_steps['6']

    print(n - total_tax)


slab_tax_1 = int(0.05 * (500_000 - 250_000))
slab_tax_2 = int(0.1 * (750_000 - 500_000))
slab_tax_3 = int(0.15 * (1_000_000 - 750_000))
slab_tax_4 = int(0.2 * (1_250_000 - 1_000_000))
slab_tax_5 = int(0.25 * (1_500_000 - 1_250_000))

slab_steps = {
    '2': slab_tax_1,
    '3': sum([slab_tax_1, slab_tax_2]),
    '4': sum([slab_tax_1, slab_tax_2, slab_tax_3]),
    '5': sum([slab_tax_1, slab_tax_2, slab_tax_3, slab_tax_4]),
    '6': sum([slab_tax_1, slab_tax_2, slab_tax_3, slab_tax_4, slab_tax_5])
}

T = int(input())

for _ in range(T):
    N = int(input())
    net_income(N)
