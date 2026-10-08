# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

import random

# TODO: secret value is hardcoded. It needs to be read from an
# environment file or other temporary source instead of included
# in the code.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# TODO: function does not reduce the boss hp, only makes the
# hp `global` and then outputs that damage was done but never
# reduces the variable value. To fix, `b_hp` needs to be
# reduced each time `attack` is called.
def attack():
  global b_hp
  dmg = damage()
  b_hp -= dmg
  print(f"You deal {dmg} damage!")

# TODO: modify the function to prevent overhealing. The function
#  permits adding 20 to the value of p_hp if it is already above 30
# which results in a health value over 50. The function should check
# the final value to confirm it is <= 50. The function does not need
# to check if the player is dead already as the gameplay loop checks
# this condition.
def heal():
  global p_hp
  p_hp = min(p_hp + 20, 50)
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

  p_hp -= damage()

  # TODO: Loop needs to be expanded to check for boss or player
  # death and print appropriate victory or loss message.
  if b_hp <= 0:
    print("Victory!")
  elif p_hp <= 0:
    print("Game Over!")
