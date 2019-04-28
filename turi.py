kane = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
number_pos = []

#所持しているお札、小銭の枚数および会計時の支払い金額を入力
for i in range(len(kane)):
    if i < 4:
        number_pos.append(int(input(str(kane[i]) + '円札の枚数は? >>')))
    else:
        number_pos.append(int(input(str(kane[i]) + '円玉の枚数は? >>')))

total = int(input('支払金額は? >>'))

#お釣りの値段(Price)が与えられたとき、お釣りの貨幣の枚数を返す関数
def turi(price):
    number_turi = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(kane)):
        while(kane[i] <= price):
            number_turi[i] += 1
            price -= kane[i]
            if price == 0:
                break
    return number_turi

#会計時の値段(Total)が与えられたとき、自分が支払うことのできる貨幣の出し方を返す関数
def funcpay(pay, number_pay, number_pos, k, total):
    if k == 8:
        for i in range(number_pos[k]):
            pay += kane[k]
            number_pay[k] += 1
            if pay >= total:
                return number_pay
                break
        number_pay[k] = 0
        pay -= kane[k] * number_pos[k]
    else:
        for i in range(number_pos[k]+1):
            if i != 0:
                pay += kane[k]
                number_pay[k] += 1
            if pay >= total:
                return number_pay
                break
            l = funcpay(pay, number_pay, number_pos, k+1, total)
            tol = 0
            if l != None:
                for i in range(len(kane)):
                    tol += kane[i] + l[i]
            if tol >= total:
                return l
                break
        number_pay[k] = 0
        pay -= kane[k] * number_pos[k]

number_pay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ppay = []
pay = 0

s = 0
a = funcpay(pay, number_pay, number_pos, 0, total)
for i in range(len(kane)):
    s += kane[i] * a[i]

numturi = 10000
tol = -1
for i in range(total, s + round(total * 0.5)):
    number_pay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = funcpay(pay, number_pay, number_pos, 0, i)
    print(i, l)
    if l != None:
        tol = 0
        for i in range(len(kane)):
            tol += kane[i] * l[i]
    if numturi == 0:
        break
    elif numturi > sum(turi(tol-total)):
        minipay = tol
        numturi = sum(turi(tol-total))

if numturi == 0:
    print('ぴったり支払うことができます!')
elif tol == -1:
    print('お金が足りません!')
else:
    print(str(minipay) + '円支払えば' + str(minipay-total) + '円のお釣りが帰ってきます!')
