# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

import random

SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# TODO: function does not reduce the boss hp, only makes the
# hp `global` and then outputs that damage was done but never
# reduces the variable value. To fix, `b_hp` needs to be
# reduced each time `attack` is called.
def attack():
  global b_hp
  b_hp -= damage()
  print("You deal 10 damage!")

def heal():
  global p_hp
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# TODO: Add dmg function that generates and returns random
# dmg values from 1 to 10 for use by the `attack` function
# and the game loop to reduce the boss and player health
# values
def damage():
    return random.randint(1,10)

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
