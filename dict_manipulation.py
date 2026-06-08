tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

is_Canada = 'Canada' in tlds
is_France = 'France' in tlds

tlds['Sweden'] = 'sw'

print(is_Canada)
print(is_France)
print()

tlds['Sweden'] = 'se'
for keys, values in tlds.items():
    print(f"{keys}: {values}")

print()
print(tlds)
