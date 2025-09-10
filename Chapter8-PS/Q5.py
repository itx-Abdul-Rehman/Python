# write a function to convet inches to cm
#  1-inche =  2.54

def inchesToCm(inches):
    cm=inches*2.54
    return cm

inches=float(input('Enter inches:'))

cm=inchesToCm(inches)
print(f'{inches}inches is equal to {cm}cm ')