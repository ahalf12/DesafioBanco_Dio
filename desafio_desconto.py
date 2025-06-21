descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Informe o preço do produto: ").strip())
cupom = input("Informe o cupom de Desconto: ").strip().upper()

if cupom == "DESCONTO10":
    print(f"{preco*(1-0.10):.2f}")

elif cupom == "DESCONTO20":
    print(f"{preco*(1-0.20):.2f}")

elif cupom == "SEM_DESCONTO":
    print(f"{preco:.2f}")