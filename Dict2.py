enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color':'green',
    'health': 100,
    'name': 'Mudillo',
}

all_enemy = []
print('Insert number jf enemy:')
val_enemy = int(input())
v_e = 0
for i in range(val_enemy):
    all_enemy.append(enemy)
    v_e +=1
print(v_e)
print(all_enemy)

