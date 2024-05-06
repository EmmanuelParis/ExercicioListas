import random
import time
rolagens = []

for i in range(100):
    rolagens.append(random.randint(1, 6))
    
for i in range(6):
    time.sleep(1.2)
    print(f"O número {i + 1} foi rolado {rolagens.count(i + 1)} vezes")