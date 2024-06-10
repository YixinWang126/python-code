def make_car(manufacture, type, **info):
    info['manufacture']=manufacture
    info['type']=type
    return info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)