import random
import time

def menu():
    print("\n--- CASA DE APOSTAS PYTHON ---")
    print("1 - Comprar créditos")
    print("2 - Fazer aposta simples")
    print("3 - Jogar caça-níqueis")
    print("4 - Ver saldo")
    print("5 - Sair")

def comprar_creditos(saldo):
    valor = float(input("Quanto você quer comprar de créditos? R$ "))
    saldo += valor
    print(f"Você comprou R$ {valor:.2f} em créditos.")
    return saldo

def aposta_simples(saldo):
    if saldo <= 0:
        print("Você não tem créditos suficientes! Compre mais para jogar.")
        return saldo

    aposta = float(input("Quanto deseja apostar? R$ "))
    if aposta > saldo:
        print("Saldo insuficiente!")
        return saldo

    # Agora com 30% de chance de vitória
    chance = random.random()  # valor entre 0 e 1
    if chance < 0.3:
        ganho = aposta * 2
        saldo += aposta  # lucro de 100%
        print(f"🎉 Você ganhou! Seu prêmio foi R$ {ganho:.2f}")
    else:
        saldo -= aposta
        print("😢 Você perdeu a aposta...")

    return saldo

def caca_niqueis(saldo):
    if saldo <= 0:
        print("Você não tem créditos suficientes! Compre mais para jogar.")
        return saldo

    aposta = float(input("Quanto deseja apostar no caça-níqueis? R$ "))
    if aposta > saldo:
        print("Saldo insuficiente!")
        return saldo

    simbolos = ["🍒", "🍋", "🔔", "🍀", "⭐"]
    roleta = [random.choice(simbolos) for _ in range(3)]

    print("Girando os rolos...")
    time.sleep(1)
    print(" | ".join(roleta))

    # Regras do caça-níqueis
    if roleta[0] == roleta[1] == roleta[2]:
        ganho = aposta * 5
        saldo += ganho - aposta
        print(f"🎰 JACKPOT! Três iguais! Você ganhou R$ {ganho:.2f}")
    elif roleta[0] == roleta[1] or roleta[1] == roleta[2] or roleta[0] == roleta[2]:
        ganho = aposta * 2
        saldo += ganho - aposta
        print(f"✨ Duas iguais! Você ganhou R$ {ganho:.2f}")
    else:
        saldo -= aposta
        print("💀 Nenhuma igual, você perdeu!")

    return saldo

def main():
    print("🎲 Bem-vindo à Casa de Apostas Python 🎲")
    nome = input("Digite seu nome: ")
    saldo = float(input("Saldo inicial (em R$): "))

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = comprar_creditos(saldo)
        elif opcao == "2":
            saldo = aposta_simples(saldo)
        elif opcao == "3":
            saldo = caca_niqueis(saldo)
        elif opcao == "4":
            print(f"💰 Seu saldo atual é R$ {saldo:.2f}")
        elif opcao == "5":
            print(f"Saindo... {nome}, seu saldo final é R$ {saldo:.2f}")
            break
        else:
            print("Opção inválida!")

main()
