def instrucao():
  print(' 7 I 8 I 9 \n --+---+-- \n 4 I 5 I 6 \n --+---+-- \n 1 I 2 I 3')
  print('Estas são as opções de jogo, escolha apenas os numeros')

jogobranco = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
]
cont_jogada = 0
print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
jogada = input('Qual sua jogada? ')
jogador1 = 'X'
jogador2 = 'O'

def ganhou():
  if jogobranco[0][2] == jogobranco[1][2] == jogobranco[2][2] == vitoria[0][2] == vitoria[1][2] == vitoria[2][2]:
    print('Ganhou')
    return fim()
  else:
    pass

vitoria = [
           [' ',' ','X'],
           [' ',' ','X'],
           [' ',' ','X'],
]
while True:
  if jogobranco[0][2] == jogobranco[1][2] == jogobranco[2][2] == vitoria[0][2] == vitoria[1][2] == vitoria[2][2]:
    print('O {} Ganhou'.format(jogador1))
    break
  else:
    if '7' == jogada:
      if jogobranco[0][0] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[0][0] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '8' == jogada:
      if jogobranco[0][1] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[0][1] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '9' == jogada:
      if jogobranco[0][2] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[0][2] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '4' == jogada:
      if jogobranco[1][0] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[1][0] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '5' == jogada:
      if jogobranco[1][1] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[1][1] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '6' == jogada:
      if jogobranco[1][2] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[1][2] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '1' == jogada:
      if jogobranco[2][0] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[2][0] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '2' == jogada:
      if jogobranco[2][1] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[2][1] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '3' == jogada:
      if jogobranco[2][2] == 'X':
        print('Ja esta marcado, jogue em outra posição')
        jogada = input('Qual sua jogada? ')
      else:
        jogobranco[2][2] = jogador1
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[0][0],jogobranco[0][1], jogobranco[0][2]))
        print('  {} I {} I {} \n  --+---+--'.format(jogobranco[1][0],jogobranco[1][1], jogobranco[1][2]))
        print('  {} I {} I {}'.format(jogobranco[2][0],jogobranco[2][1], jogobranco[2][2]))
        cont_jogada+= 1
        jogada = input('Qual sua jogada? ')
    elif '0' == jogada:
      print('Saindo...')
      break
    else:
      print('Esta opção não é valida!')
      jogada = input('Qual sua jogada? ')


def fim():
  print('-=-'*6)
  print('Houve {} jogada(s)'.format(cont_jogada))
  print('-=-'*6)
  breakpoint()
