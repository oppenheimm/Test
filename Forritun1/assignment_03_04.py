# Author: <Tómas Bragi Þorvaldsson> 
# Date: <2.1.2023> 
# Project: <skilaverk 3 d 2> 
# Acknowledgements: fekk mikla hjalp af stackoverflow i þessu dæmi

initial_input = input("Initial position: ")
movement_input = input("Movement: ")

def move(position,movement):
  x,y = position
  for m in movement:
    if m in ['r', 'R']:
      x += 1
    elif m in ['l', 'L']:
      x -= 1
    elif m in ['u', 'U']:
      y += 1
    elif m in ['d', 'D']:
      y -= 1
  return (x,y)

  

x,y = map(int, initial_input.split(","))
position = (x,y)
print(f"initial position: ({initial_input[0]},{initial_input[1]})")
movement = movement_input.strip()
final = move(position,movement)
print(f"Final position: ({final[0]},{final[1]})")