import random
from time import *

print("="*38)
print("Bem vindo ao BlackJack do Bar Seu Jorge");
print("="*38)

# Variavel do Baralho
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
random.shuffle(deck)
#====================

def play():
	"""Função Principal, função jogar o game"""
	d_cards = []
	p_cards = []

	while len(d_cards) != 2: # Mostrar cartas do Dealer
		random.shuffle(deck)
		d_cards.append(deck.pop())
		if len(d_cards) == 2:
			print("*"*28)
			print("Dealer: X - {}".format(d_cards[1]));
			print("--")
			pass

		pass

	while len(p_cards) != 2: # Mostrar as cartas
		random.shuffle(deck)
		p_cards.append(deck.pop())
		if len(p_cards) == 2:
			print("Suas Cartas: {} - {}".format(p_cards[0], p_cards[1]))
			print("Total: ", sum(p_cards))
			print("*"*28)
			pass
		pass
	pass
	sleep(3)


	""" Verificação de Derrota ou Vitória Inicial """
	if sum(p_cards) > 21 or sum(d_cards) == 21:
		print("=== Você Perdeu!! === /n === Dealer Vencedor ===")
		choice_game()
		pass
	if sum(d_cards) > 21:
		print("=== Você ganhou!! === /n === Dealer Perdeu!! ===")
		choice_game()
		pass
	if sum(d_cards) == 21 and sum(p_cards) == 21: # Verificação de Empate
		print("=== Empate!! ===")
		choice_game()
		pass

	def dealer_choice():
		""" Escolha do Dealer """
		""" Dev: Bom... de acordo com as regras do BlackJack, essa é ideia principal para 
			o Dealer seguir.

			Wiki: "Geralmente a regra é que o dealer deve bater até que alcance uma contagem de 17 ou mais."
			https://pt.wikipedia.org/wiki/Blackjack
		"""
		while sum(d_cards) < 17:
			random.shuffle(deck)
			d_cards.append(deck.pop())
			pass

		print(f"Você: {p_cards} = {sum(p_cards)} \n Dealer: {d_cards} = {sum(d_cards)}")
		print("*"*38)
		if sum(d_cards) == sum(p_cards): # Verificação de empate
			print("=== Empate!! ===")
			choice_game()
			pass

		if sum(d_cards) > 21 and sum(p_cards) <= 21:
			print("=== Você ganhou!!! === \n === Dealer Perdeu!! ===")
			choice_game()
			pass

		elif sum(d_cards) > sum(p_cards):
			print("=== Você Perdeu!!! === \n === Dealer Ganhou!! ===")
			choice_game()
			pass

		elif sum(d_cards) < sum(p_cards):
			print("=== Você Ganhou!!! === \n === Dealer Perdeu!! ===")
			choice_game()
			pass

		pass

	def player_choice():
		""" Escolha do Player """
		while sum(p_cards) < 21:
			print(f"Total: {p_cards[0]} - {p_cards[1]} = {sum(p_cards)}")
			res = int(input(f"{'='*28} \n  1. Mais carta  \n  2. Parar  \n {'='*28} \n   R= "))
			if res == 1:
				random.shuffle(deck)
				p_cards.append(deck.pop())
				res = 0

				if sum(p_cards) > 21:
					print(f"Você: {p_cards} = {sum(p_cards)} \n Dealer: {d_cards} = {sum(d_cards)}")
					print("="*32)
					print("=== Você Perdeu!!! === \n === Dealer Ganhou!! ===")
					choice_game()
				
			elif res == 2:
				dealer_choice()
			else:
				player_choice()
				pass
			pass
		pass
		dealer_choice()


	player_choice()

sleep(2)

def choice_game():
	""" Function para saber se deve-se jogar de novo. """
	answer = str(input("vamos jogar uma partida? (s/n)"));
	if answer == "s":
		play()
	elif answer == "n":
		print("Então cai fora do meu Bar!!")
		exit()
	else:
		choice_game()
	pass
choice_game()
