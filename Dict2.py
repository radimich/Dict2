enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color':'green',
    'health': 100,
    'name': 'Mudillo',
}

all_enemy = []
print('Insert number of enemy:')
val_enemy = int(input())
v_e = 0
for i in range(val_enemy):
    enemy['loc_x']=enemy['loc_x']+int(v_e)
    all_enemy.append(enemy)
    v_e +=1
for en in all_enemy:
    print(en)
print(v_e)


