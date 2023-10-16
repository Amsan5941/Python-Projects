import random

class Nim:
  def __init__(self,player,stones,computer):
    self.player=player 
    self.stones=stones
    self.computer=computer

  def board (self):
    if self.stones>0:
      self.stones-=self.player
      return self.stones

  def tech(self):
    if self.stones>0:
      self.stones-=self.computer
      return self.stones

stones=random.randint(15,30)
print('There are {} stones'.format(stones))

while True:
  player_move=int(input("Enter the amount of stones you want to take: "))
  computer=random.randint(1,3)

  x=Nim(player_move,stones,computer)

  if player_move>stones:
    print('Invalid number')

  else:
    print(x.board())
    print('Computer chose:{}'.format(computer))
    stones=x.tech()
    print(stones)

  if stones==None:
    print("No more stones")
    break