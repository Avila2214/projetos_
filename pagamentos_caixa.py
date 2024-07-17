print("{:=^40}".format("BLACK STICKER"))

preço = float(input("Digite o valor da compra: R$"))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x nou mais no cartão''')
opção = int(input("Opção de pagamento:"))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print("O valor a ser pago é de {}".format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print("O valor a ser pago é de {}".format(total))
elif opção == 3:
    total = preço
    print("O valor a ser pago é de {}".format(total))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra sera parcelada em {}x de RS{:.2f} COM JUROS".format(totalparc, parcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço, total))
else:
    print("OPÇÃO INVALIDA!")