# 12 Trade Commissions
city = input()
sales = float(input())
commission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = sales * 0.05
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.045
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.055
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = sales * 0.07
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.075
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.08
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = sales * 0.08
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.1
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.12
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif sales > 10000:
    if city == "Sofia":
        commission = sales * 0.12
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.13
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.145
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
else:
    print("error")
