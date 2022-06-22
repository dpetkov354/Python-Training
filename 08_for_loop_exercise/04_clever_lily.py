# 4 Clever Lily
age = int(input())
price_wm = float(input())
price_toy = int(input())
toy_count = 0
money_count = 0
brother_cut = 0
money_sum = 0
if 1 <= age <= 77:
    if 0 <= price_toy <= 40:
        for i in range(1, age + 1):
            if i % 2 == 0:
                money_count += 10
                money_sum += money_count
                brother_cut += 1
            else:
                toy_count += price_toy

        savings = (money_sum + toy_count) - brother_cut

        if savings >= price_wm:
            print(f'Yes! {(savings - price_wm):.2f}')
        else:
            print(f'No! {abs(savings - price_wm):.2f}')

    else:
        quit()
else:
    quit()
