# Calculadora de gorjetas

print("Bem-vindo(a) à calculadora de gorjetas!")
valor_total_da_conta = float(input("Qual foi o valor total da conta? R$ "))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? (ex. 10%, 15%, ...) "))
quantas_pessoas = int(input("Quantas pessoas irão pagar a conta: "))
pagamento_por_pessoa = (valor_total_da_conta * (1 + gorjeta / 100)) / quantas_pessoas
print(f"Cada pessoa irá pagar R${pagamento_por_pessoa:5.2f}")

