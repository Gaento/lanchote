from time import sleep

loja = "LANCHONETE DO GABRIEL"
opcoes = str(f"{'CODIGO':<10} {'ESPECIFICAÇÃO':<20} {'PREÇO':<15}")
um = 4.00
dois = 4.50
tres = 5.00
quatro = 2.00
cinco = 1.50
total = 0.0


print("-" * len(loja))
print(loja)
print("-" * len(loja))
sleep(0.7)
print()
print("-" * len(opcoes))
sleep(0.3)
print("CARDÁPIO DA LANCHONETE")
print()
sleep(0.6)
print(opcoes)
sleep(0.8)
print(f"{'1':<10} {'Cachorro Quente':<20} {'R$ 4.00':<10}")
sleep(0.6)
print(f"{'2':<10} {'X-Salada':<20} {'R$ 4.50':<10}")
sleep(0.6)
print(f"{'3':<10} {'X-Bacon':<20} {'R$ 5.00':<10}")
sleep(0.6)
print(f"{'4':<10} {'Torrada simples':<20} {'R$ 2.00':<10}")
sleep(0.6)
print(f"{'5':<10} {'Refrigerante':<20} {'R$ 1.50':<10}")
sleep(0.6)
print("-" * len(opcoes))
sleep(0.7)


while True:
    pedido = int(input("O que o senhor(a) gostaria da nossa lanchonete? (escolha pelo código): "))
    sleep(0.3)
    print()
    if pedido == 1:
        total += um
    elif pedido == 2:
        total += dois
    elif pedido == 3:
        total += tres
    elif pedido == 4:
        total += quatro
    elif pedido == 5:
        total += cinco
    else:
        print("Código inválido. Tente novamente.")
        continue
    
    
    algo_mais = input("Gostaria de mais algo senhor(a)? [S/N]: ").strip().upper()[0]
    sleep(0.3)
    print()
    
    if algo_mais == "N":
        print("Obrigado pelo pedido! Tenha um ótimo dia!")
        break
    elif algo_mais == "S":
        continue
    else:
        print("Resposta inválida. Por favor, responda com 'S' ou 'N'.")


sleep(0.4)
print(f"O total da sua conta ficou em: R$ {total:.2f}")
sleep(0.7)


while True:
    pagamento = str(input("Qual seria a forma de pagamento? [A] para Dinheiro, [B] para cartão e [C] para pix. ")).strip().upper()[0]
    sleep(0.3)
    print()
    
    if pagamento == "A":
        print(f"Sua refeição custou R${total:.2f} e foi paga com dinheiro!")
        sleep(0.3)
        break
    elif pagamento == "B":
        while True:
            forma = str(input("Débito ou Crédito? [D] para Débito e [C] para Crédito. ")).strip().upper()[0]
            sleep(0.3)
            print()
            if forma == "D":
                print(f"Sua refeição custou R${total:.2f} e foi paga no Débito!")
                sleep(0.3)
                break
            elif forma == "C":
                while True:
                    parcela = str(input("Gostaria de parcelar? [S/N] ")).strip().upper()[0]
                    sleep(0.3)
                    print()
                    if parcela == "S":
                        vezes = int(input("Em quantas vezes? (no max 10x sem juros) "))
                        sleep(0.3)
                        print()
                        if vezes <= 10:
                            parcelado = total / vezes
                            print(f"Sua refeição custou R${total:.2f} e foi parcelada em {vezes}x, cada parcela custará R${parcelado:.2f}")
                            break
                        else:
                            print("Número máximo de parcelas é 10. Tente novamente.")
                    elif parcela == "N":
                        print(f"Sua refeição custou R${total:.2f} e foi paga no Crédito!")
                        sleep(0.3)
                        break
                    else:
                        print("Resposta inválida. Por favor, responda com 'S' ou 'N'.")
                break
            else:
                print("Resposta inválida. Por favor, responda com 'D' ou 'C'.")
        break
    elif pagamento == "C":
        print(f"Sua refeição custou R${total:.2f} e foi paga no PIX!")
        sleep(0.3)
        break
    else:
        print("Opção inválida. Por favor, escolha entre [A], [B] ou [C].")
sleep(1)
print("Muito obrigado por comprar na LANCHONETE DO GABRIEL! Volte sempre.")
