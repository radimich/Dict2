enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color':'green',
    'health': 100,
    'name': 'Mudillo',
}

print('location X = '+str(enemy['loc_x']))
print('location Y = '+str(enemy['loc_y']))
print('His name is :'+str(enemy['name']))

enemy ['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print((enemy))

enemy['loc_x'] +=40
enemy['health'] -=  30
if enemy['health']<80:
    enemy['color'] = 'yellow'
print(enemy)
enemy['flag'] = 'white_blue_red'
print(enemy)