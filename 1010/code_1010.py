codigo1, quantidade1, preco1 = input().split()


codigo2, quantidade2, preco2 = input().split()


total = int(quantidade1) * float(preco1) + int(quantidade2) * float(preco2)


print("VALOR A PAGAR: R$ {:.2f}".format(total))